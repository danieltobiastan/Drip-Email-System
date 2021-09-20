import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

"""
This is just to check if you have .env file in your working directory
"""

if os.path.exists(".env"):
    load_dotenv()
else:
    print("Missing .env file in the current working directory")

""" 
Send emails based on the given parameters 

:param list_of_emails: list of email or just one long string
:param str email template: the SendGrid template of the email
:param str subject: the subject of the email in string

:return
- currently no returns but prints the response

# TODO
- possibly add placeholder based on email template as a parameter.
- check by response / exception code to check is the email was sent
"""


def send_email(list_of_emails, email_template, subject):
    # build email
    message = Mail(
        # we will need to put the from email into the .env file
        from_email="chenjack208@gmail.com",
        to_emails=list_of_emails,
        subject=subject,
    )

    try:
        message.template_id = email_template
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
