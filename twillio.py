from twilio.rest import Client

# === Replace these with your real Twilio credentials ===
account_sid = 'xxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxx'

# Create the Twilio client
client = Client(account_sid, auth_token)

# === Replace this with the Twilio number you purchased ===
twilio_number = '+13802206696'

# Fetch the latest 5 messages received by your Twilio number
messages = client.messages.list(to=twilio_number, limit=5)

# Print the details
for msg in messages:
    print(f"From: {msg.from_}")
    print(f"To: {msg.to}")
    print(f"Date: {msg.date_sent}")
    print(f"Body: {msg.body}")
    print("="*40)
