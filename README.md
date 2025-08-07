# 🛒 AI Cart Recovery Workflow

This project is an **AI-powered Cart Recovery System** that uses [`n8n`](https://n8n.io/) to automate recovery actions like sending personalized emails and phone calls when a customer abandons their cart.

---

## 📌 Features

- 🧠 Smart form to collect user info (name, email, phone, and products)
- 📦 MongoDB integration to log or fetch cart data
- 📧 Automated email reminders using dynamic templates
- 📞 Twilio-powered phone call trigger
- 🔁 Fully automated via `n8n` workflow

---

## 🚀 Workflow Preview

### 🔁 Flow Overview (n8n)

```text
[ Execute Workflow ]
        ↓
     [ MongoDB ]
        ↓
   [ Send Email ]
        ↓
  [ Make a Call ]
🧩 Components Used
Trigger: When clicking "Recover Cart"

MongoDB: Fetches or logs the cart data

Email Node: Sends personalized email reminders

Twilio Call Node: Makes a follow-up call for cart recovery

🖼️ Screenshots
🧾 Frontend: AI Cart Recovery Form

📧 Email Sent

🔁 n8n Workflow

🧰 Tech Stack
Tech	Description
n8n	Workflow automation platform
MongoDB	Cart data storage
Twilio	Call automation
SMTP / Gmail	Email sending
HTML / CSS	Frontend UI
Node.js	Backend (optional integration)

📥 How It Works
User fills the form with their name, email, number, and products.

Workflow triggers on "Recover Cart" button click.

MongoDB node optionally stores or fetches cart info.

Email node sends a recovery email to the user.

Call node (Twilio) initiates a follow-up call.

📂 Folder Structure
pgsql
Copy
Edit
.
├── README.md
├── frontend/
│   └── index.html
├── n8n-workflow/
│   └── cart-recovery.json
├── assets/
│   ├── form.png
│   ├── email.png
│   └── workflow.png
📦 Setup Instructions
🔗 Prerequisites
MongoDB URI

n8n hosted locally or on cloud

SMTP email credentials (e.g. Gmail App Password)

Twilio account with verified number

⚙️ Steps
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-cart-recovery.git
cd ai-cart-recovery
Open n8n, and import cart-recovery.json under Workflows.

Set your environment variables or credentials in n8n:

MongoDB credentials

SMTP credentials for email

Twilio credentials for call

Launch the frontend:

bash
Copy
Edit
cd frontend
open index.html
Test the form. Fill in the details and click Recover Cart to trigger the full workflow.

📧 Sample Email Output
vbnet
Copy
Edit
Hi Vivek,

We noticed you left some amazing deals behind! Your shoes and crocks are still waiting in your cart. 
As a friendly reminder, our flash deal on shoes ends in 24 hours, and you can get 20% off on your entire order!

Don't miss out on this incredible opportunity. Complete your order now and get ready to step out in style!

Complete Your Order Now

Love shopping? Explore more options on:
Flipkart | Meesho | Amazon | Zivame | Myntra

Best regards,  
Vivek LLM 🤖
🙌 Credits
Developed by Vivek Chaudhari

Automation powered by n8n

Voice & Email by Twilio and Gmail SMTP

📝 License
This project is licensed under the MIT License.

📣 Feedback
Feel free to open an issue or submit a PR for enhancements!
