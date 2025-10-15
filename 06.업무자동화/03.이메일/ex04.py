from imap_tools import MailBox
from account import *

box = MailBox('imap.gmail.com', 993)
box.login(EMAIL_ADDRESS, APP_PASSWORD, initial_folder='INBOX')

for msg in box.fetch(limit=2, reverse=True):
    print('제목:', msg.subject)
    print('내용:', msg.text)

    for att in msg.attachments:
        # print('첨부파이름:', att.filename)
        # print('타입:', att.content_type)
        #첨부파일 다운로드
        with open('download_' + att.filename, 'wb') as file:
            file.write(att.payload)
            print(f'첨부파일 {att.filename} 다운로드 완료')
    print('-' * 50)