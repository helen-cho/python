import requests
from bs4 import BeautifulSoup
import os

path = os.getcwd() + '/data/hollys'
if not os.path.exists(path):
    os.mkdir(path)

url='https://www.hollys.co.kr/menu/espresso.do'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

ul = soup.find('ul', attrs={'id':'menuSmallList'})
imgs = ul.find_all('img')

for idx, img in enumerate(imgs):
    url = 'https:' + img['src']
    res = requests.get(url)

    file_name = path + f'/menu{idx+1:02d}.jpg'
    with open(file_name, 'wb') as file:
        file.write(res.content)