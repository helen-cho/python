import requests
from bs4 import BeautifulSoup

#네이버 주식 TOP 종목
url = 'https://finance.naver.com/'
res =  requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

es = soup.find('tbody', attrs={'id':'_topItems1'}).find_all('tr', limit=5)
for e in es:
  title = e.find('a').get_text()
  td = e.find_all('td')
  price = td[0].get_text()
  updown = td[1].get_text()
  rate = td[2].get_text()
  print(title, price, updown, rate.strip())