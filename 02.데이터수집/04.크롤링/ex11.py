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

store = browser.find_element(By.ID, 'storeListUL')
lis = store.find_elements(By.TAG_NAME, 'li')
lis = [li.get_attribute('data-no') for li in lis]
print(lis)