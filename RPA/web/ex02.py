from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame("iframeResult")
e = browser.find_element(By.ID, "html")
#e.click()

# browser.switch_to.default_content()
# e = browser.find_element(By.ID, "html")

if e.is_selected() == False:
  print("선택 안 되어 있으므로 선택하기")
  e.click()
else:
  print("선택되어 있으므로 아무것도 안함")

time.sleep(5)

if e.is_selected() == False:
  print("선택 안 되어 있으므로 선택하기")
  e.click()
else:
  print("선택되어 있으므로 아무것도 안함")