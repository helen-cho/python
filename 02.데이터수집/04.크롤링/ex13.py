#커피빈 매장 주소
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument('headless')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url='https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'lxml')
ul = soup.find('ul', {'id':'storeListUL'})
items = ul.find_all('li')

list=[]
for item in items:
    title = item.find('span').contents[0].strip()
    address = item.find('p', {'class':'address'}).getText().strip()
    tel = item.find('p', {'class':'tel'}).getText().strip()
    data = [title, address, tel]
    print(data)
    list.append(data)

import csv
file_name ='커피빈매장.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)
writer.writerow(['title', 'address', 'tel'])
writer.writerows(list)
