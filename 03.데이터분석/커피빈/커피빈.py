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
stores = ul.find_all('li')

list = []
for store in stores:
    name = store.find('p', {'class':'name'}).find('span').contents[0].strip()
    address = store.find('p', {'class':'address'}).getText().strip()
    tel = store.find('p', {'class':'tel'}).getText().strip()
    print(name)
    print(address)
    print(tel)
    list.append([name, address, tel])

import csv
file = open('커피빈/커피빈매장.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)
writer.writerow(['Name', 'Address', 'Tel'])
writer.writerows(list)