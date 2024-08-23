import requests
from bs4 import BeautifulSoup

#네이버 주식 인기종목 종목
url = 'https://finance.naver.com/'
res =  requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

e = soup.find('div', attrs={'class':'aside_area aside_popular'}).find('tbody')
es = e.find_all('tr')
for e in es:
  title = e.find('a').get_text()
  td = e.find_all('td')
  price = td[0].get_text()
  updown = td[1].find('em').get_text().strip()
  updownPrice = td[1].find('span', attrs={'class':'tah p11 nv01'}).get_text().strip()
  print(title, price, updown, updownPrice)