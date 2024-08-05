from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://www.naver.com/")

first_handle = browser.current_window_handle
print('first handle:', first_handle)

#카페 아이콘 클릭
browser.find_element(By.LINK_TEXT, '카페').click()

#모든 핸들 정보
handles = browser.window_handles
for handle in handles:
  browser.switch_to.window(handle)
  print(f'{handle}:{browser.title}', end='')
  print()

print('두번째 (네이버 카페) 닫기')
browser.close()

print('첫번째 (NAVER) 핸들로 돌아오기')
browser.switch_to.window(first_handle)
time.sleep(5)

#브라우저 컨트롤이 가는한지 확인
browser.get("http://daum.net")
time.sleep(5)
browser.quit()
