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

    resend.api_key = os.environ.get("RESEND_API_KEY")

    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
"to": "kennethaces011703@gmail.com",
"reply_to": email,
"subject": f"New Message from {full_name} — {subject}",
"html": f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>New Contact Message</title>
</head>
<body style="margin:0;padding:0;background-color:#0b0f1a;font-family:'Courier New',monospace;">

  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#0b0f1a;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

          <!-- Header -->
          <tr>
            <td style="padding-bottom:28px;text-align:center;">
              <p style="margin:0;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:#38bdf8;">
                Portfolio Contact
              </p>
              <h1 style="margin:10px 0 0;font-family:Arial,sans-serif;font-size:28px;font-weight:800;color:#F9FAFB;letter-spacing:-0.02em;">
                New Message<span style="color:#38bdf8;">.</span>
              </h1>
            </td>
          </tr>

          <!-- Card -->
          <tr>
            <td style="background-color:#111827;border:1px solid rgba(255,255,255,0.08);border-radius:16px;overflow:hidden;">

              <!-- Accent bar -->
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="height:3px;background:linear-gradient(90deg,#38bdf8,#818cf8);border-radius:16px 16px 0 0;"></td>
                </tr>
              </table>

              <!-- Sender info -->
              <table width="100%" cellpadding="0" cellspacing="0" style="padding:28px 32px 0;">
                <tr>
                  <td>
                    <table cellpadding="0" cellspacing="0">
                      <tr>
                        <!-- Avatar -->
                        <td style="padding-right:16px;vertical-align:top;">
                          <div style="display:flex;align-items:center;justify-content:center;text-align:center;line-height:48px;font-size:18px;font-weight:700;color:#38bdf8;font-family:Arial,sans-serif;">
                            {full_name[0].upper()}
                          </div>
                        </td>
                        <td style="vertical-align:top;">
                          <p style="margin:0;font-size:16px;font-weight:700;color:#F9FAFB;font-family:Arial,sans-serif;">{full_name}</p>
                          <p style="margin:4px 0 0;font-size:12px;color:#38bdf8;">{email}</p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <!-- Divider -->
              <table width="100%" cellpadding="0" cellspacing="0" style="padding:20px 32px 0;">
                <tr>
                  <td style="height:1px;background-color:rgba(255,255,255,0.06);"></td>
                </tr>
              </table>

              <!-- Subject -->
              <table width="100%" cellpadding="0" cellspacing="0" style="padding:20px 32px 0;">
                <tr>
                  <td>
                    <p style="margin:0 0 6px;font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:#4b5563;font-family:Arial,sans-serif;">Subject</p>
                    <p style="margin:0;font-size:15px;font-weight:600;color:#F9FAFB;font-family:Arial,sans-serif;">{subject}</p>
                  </td>
                </tr>
              </table>

              <!-- Message -->
              <table width="100%" cellpadding="0" cellspacing="0" style="padding:20px 32px 0;">
                <tr>
                  <td>
                    <p style="margin:0 0 10px;font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:#4b5563;font-family:Arial,sans-serif;">Message</p>
                    <div style="background-color:#0b0f1a;border:1px solid rgba(255,255,255,0.06);border-left:3px solid #38bdf8;border-radius:8px;padding:16px 18px;">
                      <p style="margin:0;font-size:14px;color:#9ca3af;line-height:1.8;font-family:'Courier New',monospace;">{message}</p>
                    </div>
                  </td>
                </tr>
              </table>

              <!-- Reply button -->
              <table width="100%" cellpadding="0" cellspacing="0" style="padding:24px 32px;">
                <tr>
                  <td>
                    <a href="mailto:{email}?subject=Re: {subject}"
                       style="display:inline-block;background-color:#38bdf8;color:#0b0f1a;text-decoration:none;padding:12px 28px;border-radius:8px;font-size:13px;font-weight:700;letter-spacing:0.06em;font-family:Arial,sans-serif;">
                      Reply to {full_name} →
                    </a>
                  </td>
                </tr>
              </table>

            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding-top:24px;text-align:center;">
              <p style="margin:0;font-size:11px;color:#374151;letter-spacing:0.08em;font-family:Arial,sans-serif;">
                Sent via your portfolio contact form &nbsp;·&nbsp; Jan Kenneth Fumar
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

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