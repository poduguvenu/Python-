# python -m smtpd -c DebuggingServer -n localhost:1025 --- For listening to emails on our local machines, and print out the message at the terminal

import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP('localhost', 1025) as smtp:
  # smtp.ehlo()
  # smtp.starttls()
  # smtp.ehlo()

  # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  subject = "Grab dinner this weekend?"
  body = 'How about dinner at 6pm this Saturday?'

  msg = f'Subject: {subject}\n\n{body}'

  smtp.sendmail(EMAIL_ADDRESS, 'poduguvenu@gmail.com', msg)

  