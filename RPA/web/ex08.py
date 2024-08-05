from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#다운로드 위치 지정
options.add_experimental_option("prefs", {'download.default_directory':r'C:\data\python\RPA'})

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
time.sleep(3)

browser.switch_to.frame('iframeResult')

#download 링크 클릭
e = browser.find_element(By.XPATH, '/html/body/p[2]/a')
e.click()