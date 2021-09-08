import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='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'

message = Mail(
    from_email='chenjack208@gmail.com',
    to_emails='22764884@student.uwa.edu.au',
    subject='Sending with Twilio SendGrid is Fun')
try:
    message.template_id = "d-f4a7875981ca4e63a01a35828336cf75"
    sg = SendGridAPIClient(os.environ.get(SENDGRID_API_KEY))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)