from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://flight.naver.com/")
time.sleep(3)

#1. 가는 날 선택
browser.find_element(By.XPATH, '//button[text()="가는 날"]').click()

#2. 이번달 25일 이번달 28일 선택
browser.find_elements(By.XPATH, '//b[text()="25"]')[0].click()
browser.find_elements(By.XPATH, '//b[text()="5"]')[0].click()

#3. 도착지 선택
browser.find_element(By.XPATH, '//b[text()="도착"]').click()
time.sleep(2)
browser.find_element(By.XPATH, '//button[contains(text(), "국내")]').click()
time.sleep(2)
browser.find_element(By.XPATH, '//i[contains(text(),"제주국제공항")]').click()
time.sleep(2)

#4. 항공권 검색 버튼
browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]').click()

first = 'domestic_Flight__8bR_b'
es = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, first)))
print(es.text)
browser.quit()
