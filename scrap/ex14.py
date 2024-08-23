import requests
from bs4 import BeautifulSoup
import re
def create_soup(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')
  return soup

def weather():
  url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
  soup = create_soup(url)
  temp = soup.find('div', attrs={'class':'temperature_text'})
  temp = re.sub('현재 온도','', temp.get_text()).strip()
  print(temp)
  return temp

def news():
  url='https://news.naver.com/section/105'
  soup = create_soup(url)
  es = soup.find('ul', attrs={'class':'sa_list'}).find_all('li', limit=5)
  items=[]
  for e in es:
    title = e.find('strong', attrs={'class':'sa_text_strong'}).get_text()
    link = e.find('a')['href']
    print(title)
    print(link)
    data = {'title':title, 'link':link}
    items.append(data)
  return items

def english():
  url='https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
  soup = create_soup(url)

  es = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
  korean=[]
  for e in es[:4]:
    print(e.get_text().strip())
    data = {'sentence': e.get_text().strip()}
    korean.append(data)

  english = []  
  for e in es[4:8]:
    print(e.get_text().strip())
    data = {'sentence': e.get_text().strip()}
    english.append(data)

  return {'korean':korean, 'english':english}

print(weather())
print('-' * 50)
print(news())
print('-' * 50)
print(english())
