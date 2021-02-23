import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()

  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  subject = "Grab dinner this weekend?"
  body = 'How about dinner at 6pm this Saturday?'

  msg = f'Subject: {subject}\n\n{body}'

  smtp.sendmail(EMAIL_ADDRESS, 'poduguvenu@gmail.com', msg)

