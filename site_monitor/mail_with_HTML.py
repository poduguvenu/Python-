import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()

msg['Subject'] = "Check out HTML Email!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'poduguvenu@gmail.com'
msg.set_content('This is a plain text email!')

msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
<body>
  <h1 style="color:slategray;">This is an HTML Email!</h1>
</body>
</html>
""", subtype='html')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  smtp.send_message(msg)