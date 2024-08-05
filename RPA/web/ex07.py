from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://www.w3schools.com/html/") #[구글] - [w3schools html] - [HTML Examples]

time.sleep(5)

#특정 위치(HTML Examples)로 스크롤
e = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[58]')

#방법1 : ActionChains
#actions = ActionChains(browser)
#actions.move_to_element(e).perform()

#방법2 : 좌표 정보 이용
xy = e.location_once_scrolled_into_view #함수가 아니다.
print("type : ", type(xy))
print("value : ", xy)

e.click()


