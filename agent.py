import os
import time
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
import groq

# ========== SETUP ==========

load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# GROQ API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Please check your .env file!")

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")
db = client["cart"]
recoveries = db["recoveries"]

# GROQ client setup
groq_client = groq.Client(api_key=api_key)

# ========== LLM MESSAGE GENERATOR ==========

def generate_convincing_message(username: str, product: str) -> str:
    prompt = (
        f"You're a marketing assistant. The user '{username}' showed interest in '{product}'. "
        "Write a convincing email under 100 words to get them to complete the purchase. "
        "Include urgency, current deals, and a friendly tone."
    )

    try:
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        message = response.choices[0].message.content
        return message.strip()

    except Exception as e:
        logging.error(f"🚨 Failed to generate message for {username}: {e}")
        return ""

# ========== MAIN LOGIC ==========

def process_new_documents():
    logging.info("📡 Monitoring new entries in 'recoveries' collection...")
    seen_ids = set()

    while True:
        try:
            new_entries = recoveries.find({"llm_result": {"$exists": False}})

            for doc in new_entries:
                doc_id = str(doc["_id"])
                if doc_id in seen_ids:
                    continue

                username = doc.get("username")
                product = doc.get("product")

                if not username or not product:
                    logging.warning(f"⚠️ Skipping invalid document: {doc}")
                    continue

                logging.info(f"🎯 Processing for {username}: {product}")
                message = generate_convincing_message(username, product)

                if message:
                    recoveries.update_one(
                        {"_id": doc["_id"]},
                        {"$set": {
                            "llm_result": {
                                "product_name": product,
                                "message": message
                            }
                        }}
                    )
                    logging.info(f"✅ Message saved for {username}")
                else:
                    logging.warning(f"⚠️ Message generation failed for {username}")

                seen_ids.add(doc_id)

        except Exception as err:
            logging.error(f"🚨 Error during processing: {err}")

        time.sleep(5)

# ========== ENTRY POINT ==========

if __name__ == "__main__":
    try:
        process_new_documents()
    except KeyboardInterrupt:
        logging.info("👋 Gracefully stopped by user.")
