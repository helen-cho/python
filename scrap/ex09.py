from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

browser.get('https://www.naver.com/')
e = browser.find_element(By.ID, 'query')
e.send_keys('나도코딩')
time.sleep(2)
e.send_keys(Keys.ENTER)
time.sleep(5)

browser.quit()

