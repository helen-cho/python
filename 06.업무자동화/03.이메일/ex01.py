import smtplib
from account import *

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    subject='test email'
    body='main body'
    msg = f'Subject:{subject}\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'hd9536@daum.net', msg)