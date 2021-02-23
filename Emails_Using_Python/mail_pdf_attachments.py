import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()

msg['Subject'] = "Check out PDF!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'poduguvenu@gmail.com'
msg.set_content('PDF attached...')

files = ['A sample PDF.pdf']

for file in files:
  with open(file, 'rb') as f:
    file_data = f.read()
    file_name = f.name
 
  # Sending PDF
  msg.add_attachment(file_data, maintype='application', subtype='octet_stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  smtp.send_message(msg)