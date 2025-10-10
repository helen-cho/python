from selenium import webdriver
from selenium.webdriver.common.by import By

import time

brower = webdriver.Chrome()
brower.get('http://naver.com')

btn = brower.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')

btn.click()
time.sleep(3)

brower.back()
brower.forward()
brower.refresh()

time.sleep(10)