from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
time.sleep(2)

browser.switch_to.frame("iframeResult")
e = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
e.click()
time.sleep(3)

e = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Volvo"]')
e.click()
time.sleep(3)

e = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
e.click()

