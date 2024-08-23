from flask import Blueprint, render_template, request
import json

bp = Blueprint('crawl', __name__, url_prefix='/crawl')

def browser_config(url, query):
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

  browser.get(url)
  e = browser.find_element(By.ID, 'queryInputHeader')
  e.send_keys(query)
  e.send_keys(Keys.ENTER)
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(browser.page_source, 'lxml')
  return soup

@bp.route('/house.json')
def houseJson():
  args = request.args
  query = args['query']
  url='https://land.naver.com/'
  soup=browser_config(url, query)

  es = soup.find_all('div', attrs={'class':'item'})
  items = []
  for e in es:
    title = e.find('div', attrs={'class':['title','item_title']})
    if title:
      title=title.get_text()
    else:
      title=''  
    address=e.find('div', attrs={'class':'address'})
    if address:
      address = address.get_text()
    else:
      address =''   
    info = e.find('div', attrs={'class':'info_area'})
    if info:
      info = info.get_text()
    else:
      info =''
    item={'title':title, 'address':address, 'info':info}
    items.append(item)
  return items

@bp.route('/house')
def house():
  return render_template('index.html', 
      title='부동산검색', pageName='crawl/house.html')


from routes import ex14

@bp.route('/news')
def news():
  result = json.dumps(ex14.news(), indent=4, ensure_ascii=False)
  return result

@bp.route('/weather')
def weather():
  return ex14.weather()

@bp.route('/english')
def english():
  result = json.dumps(ex14.english(), indent=4, ensure_ascii=False)
  return result