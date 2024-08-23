from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url='https://land.naver.com/'
browser.get(url)

e = browser.find_element(By.ID, 'queryInputHeader')
e.send_keys('DMC아트포레자이')
e.send_keys(Keys.ENTER)

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')

es = soup.find_all('div', attrs={'class':'item'})
for e in es:
  title = e.find('div', attrs={'class':'title'})
  address=e.find('div', attrs={'class':'address'})
  if title:
    title=title.get_text()
  else:
    title=''  
  if address:
    address = address.get_text()
  else:
    address =''   
  info = e.find('div', attrs={'class':'info_area'})
  if info:
    info = info.get_text()
  else:
    info =''

  print(title)
  print(address)
  print(info)
  print('검색수:' , len(es))
  print('-' * 50)
print(len(es))
browser.quit()
