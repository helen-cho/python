from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
time.sleep(2)

browser.switch_to.frame("iframeResult")
e = browser.find_element(By.ID, "vehicle1")

if e.is_selected() == False:
  print("선택 안 되어 있으므로 선택")
  e.click()
else:
  print("선택되어 있으모로 아무것도 안 함")

time.sleep(10)