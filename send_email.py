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

:param list email_batches: list of different email batches to send at specific times

:return
- currently no returns but prints the response

# TODO
- set a time to run this function
- possibly add placeholder based on email template as a parameter.
- check by response / exception code to check is the email was sent
"""

"chenjack208@gmail.com"

def send_email(email_batches):
    pass
    # # build email
    # message = Mail(
    #     # we will need to put the from email into the .env file
    #     from_email=email_from,
    #     to_emails=email_to,
    #     subject=subject,
    # )
    #
    # try:
    #     message.template_id = email_template
    #     sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #     print(e)
