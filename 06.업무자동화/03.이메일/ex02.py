import smtplib
from account import *
from email.message import EmailMessage

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)

    msg = EmailMessage()
    msg['Subject']='테스트 제목입니다.'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'cho9536@gmail.com'
    msg.set_content('테스트 내용입니다.')
    smtp.send_message(msg)