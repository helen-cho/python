import requests
from bs4 import BeautifulSoup

def weather_temp():
  url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8'
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')

  temp = soup.find('div', {'class':'temperature_text'})
  if temp:
    temp = temp.get_text()
  else:
    temp='없음'
  return temp  

def exechage_rate():
  url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8'
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')
  rate = soup.find_all('span', attrs={'class': 'nb_txt _pronunciation'})
  if rate:
    rate = rate[1].get_text()
  else:
    rate = '없읍'
  return rate

def stock(input_text):
  index = input_text.find('주식')
  query=input_text[:index+2]
  url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=' + query
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')
  price = soup.find('div', attrs={'class':'spt_tlt'}).find('span', attrs={'class':'spt_con'})
  if price:
    price = price.get_text()
  else:
    price = '없음'
  return price

