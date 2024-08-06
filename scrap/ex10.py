from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

browser.get('https://flight.naver.com/')
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
e.click()

#이번달(28) 클릭
es = browser.find_elements(By.XPATH, '//b[text()="28"]')
es[0].click()
es = browser.find_elements(By.XPATH, '//b[text()="30"]')
es[0].click()

#도착버튼클릭
e = browser.find_element(By.XPATH, '//b[text()="도착"]')
e.click()
time.sleep(2)

#국내클릭
e = browser.find_element(By.XPATH, '//button[text()="국내"]')
e.click()
time.sleep(2)

#제주국제공항
e = browser.find_element(By.XPATH, '//i[contains(text(),"제주국제공항")]')
e.click()
time.sleep(2)

#항공권검색
e = browser.find_element(By.XPATH, '//span[contains(text(), "검색")]')
e.click()

time.sleep(10)
e = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]')
print(e.text)

browser.quit()