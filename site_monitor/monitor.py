import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def notify_user():
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'YOUR SITE IS DOWN!'
    body = 'Make sure the server restarted and it is back up'
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'poduguvenu@gmail.com', msg)

def reboot_server():
  client = LinodeClient(LINODE_TOKEN)
  my_server = client.load(Instance, 376715)
  my_server.reboot()

try:
  r = requests.get('https://coreyms.com', timeout=5)
  
  if r.status_code != 200:
  notify_user()
  reboot_server()

except Exception as e:
  notify_user()
  reboot_server()  



  
