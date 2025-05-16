# Mailing Client Project: Sends Mails

# Imports
import smtplib
from dotenv import load_dotenv
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

load_dotenv()
email = os.getenv('SENDER_EMAIL')
rec_email = os.getenv('RECIEVER_EMAIL')
password = os.getenv('PASSWORD')
# Attach image optionally
image_path = "img.jpg"

# Start Server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

# Login
server.login(email, password)

msg = MIMEMultipart()
msg['From'] = "PotatoBox"
msg['To'] = rec_email
msg['Subject'] = "Something Something"

with open("msg.txt", 'r') as f:
    message = f.read()

# Attach message
msg.attach(MIMEText(message, 'plain'))

# Attach image
attachment = open(image_path, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={image_path}')
msg.attach(p)

text = msg.as_string()

# Send Mail and Exit Server
server.sendmail(email, rec_email, text)
server.quit()