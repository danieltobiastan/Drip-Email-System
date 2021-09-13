import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

if os.path.exists('.env'):
    load_dotenv()
    message = Mail(
        from_email="chenjack208@gmail.com",
        to_emails="22764884@student.uwa.edu.au",
        subject="Sending with Twilio SendGrid is Fun",
    )
    try:
        message.template_id = "d-f4a7875981ca4e63a01a35828336cf75"
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

else:
    pass
