import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='파일첨부 예제'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'cho9536@gmail.com'
msg.set_content('파일을 첨부합니다.')

with open('manage.png', 'rb') as file:
    msg.add_attachment(file.read(), maintype='image', subtype='png', 
                       filename=file.name)

#구글 - MIME Type
with open('sample.xlsx', 'rb') as file:
    msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', 
                       filename=file.name)
    
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
    smtp.send_message(msg)
