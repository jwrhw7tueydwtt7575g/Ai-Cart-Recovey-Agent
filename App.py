# from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env
# load_dotenv()

# # Flask setup
# app = Flask(__name__)

# # MongoDB connection
# client = MongoClient("mongodb+srv://vivekchaudhari3718:vivekchaudhari3718@cluster1.9qlun5j.mongodb.net/")
# db = client["Cart"]
# collection = db["recoveries"]
# print("Connected to MongoDB")

# # Setup Groq client
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise ValueError("Missing GROQ_API_KEY in .env file")
# client_llm = Groq(api_key=GROQ_API_KEY)


# def generate_convincing_email(username, product_list):
#     prompt = (
#         f"You're an expert marketing assistant. The user '{username}' added these items to the cart: "
#         f"{', '.join(product_list)} but didn't complete the purchase.\n\n"
#         "Write a **concise, friendly, high-converting email (60–80 words)** that:\n"
#         "- Mentions at least one **current deal or price advantage** (e.g., Amazon price drop, flash deal, bundle offer).\n"
#         "- Creates a sense of **urgency** (e.g., limited stock, time-limited offer).\n"
#         "- Stays polite and persuasive without being pushy.\n"
#         "- Ends with a clear **call to action** (e.g., 'Complete Your Order Now').\n\n"
#         "At the end of the email, add clickable links to the same or similar items from these platforms:\n"
#         "- Flipkart: https://www.flipkart.com/\n"
#         "- Meesho: https://www.meesho.com/\n"
#         "- Amazon: https://www.amazon.in/\n"
#         "- Zivame: https://www.zivame.com/\n"
#         "- Myntra: https://www.myntra.com/\n\n"
#         "Finally, close the email with:\n"
#         "Best regards,\nVivek LLM 🤖\n\n"
#        "Output only the email content. Do not include any explanation, title, or introduction."
#     )

#     response = client_llm.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7,
#         max_tokens=250
#     )
#     return response.choices[0].message.content.strip()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         username = request.form['username'].strip().lower()
#         email = request.form['email'].strip().lower()
#         phone = request.form['phone'].strip()
#         raw_products = request.form['products']
#         product_list = [p.strip().lower() for p in raw_products.split(',') if p.strip()]

#         # Get LLM output
#         convincing_email = generate_convincing_email(username, product_list)

#         # Store in MongoDB
#         collection.insert_one({
#             "username": username,
#             "email": email,
#             "phone": phone,
#             "products": product_list,
#             "llm_result": convincing_email
#         })

#         return redirect(url_for('thank_you'))

#     return render_template('form.html')


# @app.route('/thankyou')
# def thank_you():
#     return render_template('thankyou.html')


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from groq import Groq
from dotenv import load_dotenv
from markupsafe import escape
import os

# Load environment variables from .env
load_dotenv()

# Flask setup
app = Flask(__name__)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("Missing MONGO_URI in .env file")

client = MongoClient(MONGO_URI)
db = client["Cart"]
collection = db["recoveries"]
print("✅ Connected to MongoDB")

# Groq API setup
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env file")

client_llm = Groq(api_key=GROQ_API_KEY)

def generate_convincing_email(username, product_list):
    prompt = (
        f"You're an expert marketing assistant. The user '{username}' added these items to the cart: "
        f"{', '.join(product_list)} but didn't complete the purchase.\n\n"
        "Write a **concise, friendly, high-converting email (60–80 words)** that:\n"
        "- Mentions at least one **current deal or price advantage** (e.g., Amazon price drop, flash deal, bundle offer).\n"
        "- Creates a sense of **urgency** (e.g., limited stock, time-limited offer).\n"
        "- Stays polite and persuasive without being pushy.\n"
        "- Ends with a clear **call to action** (e.g., 'Complete Your Order Now').\n\n"
        "At the end of the email, add clickable links to the same or similar items from these platforms:\n"
        "- Flipkart: https://www.flipkart.com/\n"
        "- Meesho: https://www.meesho.com/\n"
        "- Amazon: https://www.amazon.in/\n"
        "- Zivame: https://www.zivame.com/\n"
        "- Myntra: https://www.myntra.com/\n\n"
        "Finally, close the email with:\n"
        "Best regards,\nVivek LLM 🤖\n\n"
        "Output only the email content. Do not include any explanation, title, or introduction."
    )

    response = client_llm.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=250
    )
    return response.choices[0].message.content.strip()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username'].strip().lower()
        email = request.form['email'].strip().lower()
        phone = request.form['phone'].strip()
        raw_products = request.form['products']
        product_list = [p.strip().lower() for p in raw_products.split(',') if p.strip()]

        # Validate input
        if not username or not email or not product_list:
            return "All fields are required.", 400

        # Generate email using LLM
        convincing_email = generate_convincing_email(username, product_list)
        print(f"[Generated Email] {convincing_email}")  # Dev log

        # Store in MongoDB
        collection.insert_one({
            "username": username,
            "email": email,
            "phone": phone,
            "products": product_list,
            "llm_result": convincing_email
        })

        return redirect(url_for('thank_you'))

    return render_template('form.html')


@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
