from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://shopping.naver.com/home")

#검색버튼을 찾아 클릭한다.
e = browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/button[2]')
e.click()

#검색어입력상자를 찾아 '무선마우스'를 입력한 후 엔터키를 친다.
e = browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
e.send_keys("무선마우스")
e.send_keys(Keys.ENTER)

interval = 2
prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  time.sleep(interval)
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if curr_height == prev_height:
    break
  prev_height = curr_height
time.sleep(interval)
browser.execute_script('window.scrollTo(0, 0)') #맨 위로 올리기

