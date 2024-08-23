from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import json

def wait_until(browser, xpath):
  WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

def create_soup(query):
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
  options.add_experimental_option('detach', True)
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()

  url='https://www.daangn.com/search/{}/'.format(query)
  browser.get(url)

  try:
    xpath = '//*[@id="result"]/div[1]/div[2]/span' #더보기
    wait_until(browser, xpath)
    e=browser.find_element(By.XPATH, xpath)
    e.click()
  except Exception as err:
    pass

  prev_height = browser.execute_script('return document.body.scrollHeight')
  while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
      print('스크롤완료!')
      break
    prev_height = curr_height

  soup = BeautifulSoup(browser.page_source, 'lxml')
  browser.quit()
  return soup

def search(query):
  soup=create_soup(query)
  es = soup.find_all('article', attrs={'class':re.compile('^flea-market-article')})
  items = []
  for index, e in enumerate(es):
    title = e.find('span', attrs={'class':'article-title'}).get_text()
    address= e.find('p', attrs={'class':'article-region-name'}).get_text().strip()
    price= e.find('p', attrs={'class':'article-price'}).get_text().strip()
    image = e.find('img')['src']
    data = {'no':index+1, 'title':title, 'address':address, 'price':price, 'image':image}
    items.append(data)
  return json.dumps(items, indent=4, ensure_ascii=False)
  
#print(search('청라'))


