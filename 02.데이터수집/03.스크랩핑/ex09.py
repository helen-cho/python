import requests
from bs4 import BeautifulSoup
import json

url='https://www.hollys.co.kr/menu/espresso.do'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

ul = soup.find('ul', attrs={'id':'menuSmallList'})
li = ul.find_all('li')

list =[]
for item in li:
    title = item.a.getText().strip()
    url = 'https:' + item.a.img['src']
    print(title, url)
    data = {'title':title, 'url':url}
    list.append(data)

file_name = 'data/menu.json'
with open(file_name, 'w', encoding='utf8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

