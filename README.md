# 🛒 AI Cart Recovery Automation using n8n, MongoDB, Twilio & Groq LLM

This project is an AI-powered **Cart Recovery System** built using the `n8n` workflow automation tool, with integrations for MongoDB, Email (SMTP), Twilio for voice calls, and the **Groq LLM API** to dynamically generate personalized marketing emails based on the abandoned cart content.

---

## 🧠 Overview

When a user abandons a shopping cart, businesses often lose sales. This automation ensures that such users are intelligently and automatically re-engaged via **email and phone call**, with content tailored to their cart contents.

This system not only reminds users to complete their purchase but also improves conversion using **LLM-generated emails** that are highly personalized and persuasive.

---

## 📋 Workflow Summary

The automation workflow is implemented using `n8n` and follows this structure:

1. **Trigger (Webhook Form Submission)**  
   A user submits their name, email, phone number, and list of abandoned cart products via a web form.

2. **MongoDB (Find/Log)**  
   The data is sent to MongoDB where it is either fetched for updates or logged for analytics and record-keeping.

3. **Groq LLM API (Email Content Generation)**  
   Using the Groq API (running powerful language models like `llama3` or `mixtral`), the product list is sent as a prompt and a **custom recovery email** is generated. This message includes urgency (e.g., limited-time discounts), mentions specific products from the user’s cart, and uses marketing-style tone to increase conversion.

4. **Send Email (SMTP)**  
   The generated email is then sent to the user via an SMTP provider like Gmail. This email includes the user's name and product list to create a personal touch.

5. **Make a Call (Twilio)**  
   After the email is sent, a voice call is made to the user using **Twilio**, with a polite reminder that they left products in their cart, encouraging them to check their email and complete the order.

---

## 🧩 Tools & Technologies Used

| Tool      | Role |
|-----------|------|
| **n8n**   | Core visual workflow automation platform |
| **MongoDB** | To store and retrieve cart data |
| **Groq LLM** | To generate personalized recovery email content dynamically |
| **SMTP (Gmail)** | To send the generated email to the user |
| **Twilio** | To call the user as a final push for recovery |
| **HTML Form** | Web UI for user cart submission |

---

## 💡 Why Use Groq LLM?

- Enables real-time **personalized email generation**.
- Embeds user-specific product names and tone.
- Improves chances of recovery with emotional, relevant content.
- Significantly better than static email templates.

---

## 💬 Example Use Case

Let’s say **Vivek** abandons a cart with **“shoes” and “crocks”**. When he submits the form:

- MongoDB logs his details.
- Groq LLM is prompted with:  
  _"Generate a friendly, urgent cart recovery email for Vivek who abandoned shoes and crocks."_
- A creative email is returned like:  
  _"Hi Vivek, you left behind amazing deals on shoes and crocks. Our flash sale ends soon — complete your order and enjoy 20% off!"_
- This email is automatically sent, and a Twilio voice call follows up within seconds.

---

## 🛠 Setup Overview

1. Set up your `n8n` environment (self-hosted or cloud).
2. Create a Webhook trigger in n8n for the form.
3. Connect MongoDB and Twilio nodes with appropriate credentials.
4. Integrate Groq API using an HTTP Request node.
5. Connect the LLM response to the Email node for dynamic content injection.
6. Test end-to-end using a local form submission.

---

## 📣 Conclusion

This AI Cart Recovery system is an **end-to-end automated sales booster** for e-commerce. By combining the flexibility of `n8n`, the power of **LLMs for contextual email generation**, and the immediacy of **voice calls**, this setup ensures that abandoned carts turn into recovered checkouts — automatically.

---

## 👨‍💻 Built by

**Vivek Chaudhari**  
AI & Automation Developer  
Email: vivekchaudhari3718@gmail.com
