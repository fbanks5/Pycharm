import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'Frantz Banks III'
email['To'] = 'frantz7101990@gmail.com'
email['Subject'] = 'Test message from python class'

email.set_content('Test message from python class')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('frantz7101990@gmail.com', '')
    smtp.send_message(email)
    print('Email sent!')