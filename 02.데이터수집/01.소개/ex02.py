import requests

url='https://www.megabox.co.kr/movie'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)

file_name='data/megabox.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)