# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:5173",
    "https://personal-website-kenezu17s-projects.vercel.app"
])
@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

    first_name = data.get("fname")
    last_name = data.get("lname")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    full_name = f"{first_name} {last_name}"

    # HTML email content
    html_content = f"""
    <html>
      <body style="font-family: Arial; background:#f4f4f4; padding:20px;">
        <div style="max-width:600px; margin:auto; background:white; padding:20px; border-radius:10px;">
          <h2 style="color:#333;">📩 New Contact Message</h2>
          <p><strong>Name:</strong> {full_name}</p>
          <p><strong>Email:</strong> {email}</p>
          <p><strong>Subject:</strong> {subject}</p>
          <hr/>
          <p><strong>Message:</strong></p>
          <p style="background:#f9f9f9; padding:10px; border-radius:5px;">
            {message}
          </p>
        </div>
      </body>
    </html>
    """

    sender_email = "jankennethfumar3@gmail.com"        
    sender_password = "xhmphxerditnwcis"       
    receiver_email = "jankennethfumar3@gmail.com"      

    msg = MIMEText(html_content, "html")
    msg["Subject"] = f"New Message from {full_name}"
    msg["From"] = f"{full_name} <{sender_email}>"
    msg["To"] = receiver_email
    msg["Reply-To"] = email  # Reply goes to sender

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return jsonify({"message": "Message sent successfully!"})

    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send message"}), 500

if __name__ == "__main__":
    app.run(debug=False)