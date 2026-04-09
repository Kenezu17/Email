from flask import Flask, request, jsonify
from flask_cors import CORS
import resend
import os

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:5173",
    "https://personal-website-kenezu17s-projects.vercel.app",
    "https://personal-website-eosin-mu.vercel.app"
])

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "Backend is running!"})

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    first_name = data.get("fname")
    last_name = data.get("lname")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")
    full_name = f"{first_name} {last_name}"

    resend.api_key = os.environ.get("re_UNBvdbe8_8Kix2mhb7XxBXpLUNuRK1nzu")

    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "jankennethfumar3@gmail.com",
            "reply_to": email,
            "subject": f"New Message from {full_name} - {subject}",
            "html": f"""
            <html>
              <body style="font-family: Arial; background:#f4f4f4; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; padding:20px; border-radius:10px;">
                  <h2 style="color:#333;">📩 New Contact Message</h2>
                  <p><strong>Name:</strong> {full_name}</p>
                  <p><strong>Email:</strong> {email}</p>
                  <p><strong>Subject:</strong> {subject}</p>
                  <hr/>
                  <p><strong>Message:</strong></p>
                  <p style="background:#f9f9f9; padding:10px; border-radius:5px;">{message}</p>
                </div>
              </body>
            </html>
            """
        })
        return jsonify({"message": "Message sent successfully!"})

    except Exception as e:
        print(e)
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)