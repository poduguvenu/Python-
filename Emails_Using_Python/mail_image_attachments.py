import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()

msg['Subject'] = "Check out pictures!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'poduguvenu@gmail.com'
msg.set_content('Images attached...')

files = ['logo.jfif', 'profile_pic.jpg']

for file in files:
  with open(file, 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

  Sending Images
  msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  smtp.send_message(msg)