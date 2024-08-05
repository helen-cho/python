from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://www.daum.net/")
# e = browser.find_element(By.LINK_TEXT, "카페")
# print(e.get_attribute("href"))
# print(e.get_attribute("class"))
# e.click()

# e = browser.find_element(By.ID, "query")
# e.send_keys("나도코딩")
# e.send_keys(Keys.ENTER)

# es = browser.find_elements(By.TAG_NAME, "a")
# for e in es:
#   print(e.get_attribute("href"))

e = browser.find_element(By.NAME, "q")
e.send_keys("나도코딩")

e = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
e.click()

browser.save_screenshot("daum.png")
#print(browser.page_source)

with open('daum.html', 'w', encoding='utf-8') as file:
  file.write(browser.page_source)

browser.close()