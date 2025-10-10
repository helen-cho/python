import requests

url='https://ssl.pstatic.net/melona/libs/1544/1544462/226b0d2c36907f712ab8_20250822151658763.jpg'
res = requests.get(url)

file_name='data/naver.jpg'
with open(file_name, 'wb') as file:
    file.write(res.content)