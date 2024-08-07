from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

def wait_until(xpath):
  WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

browser.get('https://flight.naver.com/')
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
e.click()

#이번달(28) 클릭
xpath = '//b[text()="28"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

xpath = '//b[text()="30"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

#도착버튼클릭
xpath = '//b[text()="도착"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#국내클릭
xpath = '//button[text()="일본"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#제주국제공항
xpath = '//i[contains(text(),"TYO")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#항공권검색
xpath = '//span[contains(text(), "검색")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

first = '//*[@id="container"]/div[5]/div/div[3]/div[1]/div'
wait_until(first)
e = browser.find_element(By.XPATH, first)
#print(e.text)

#검색목록
es = browser.find_elements(By.XPATH, '//*[contains(@class,"concurrent_ConcurrentItemContainer__NDJda")]')
es = es[:10]
for e in es:
  print(e.text)
  print('-' * 50)
print("전체검색수:", len(es))

browser.quit()

