from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#1. URL 접속
browser.get("https://www.w3schools.com/")

#2. LEARN HTML 클릭
e = browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]')
e.click()

#3. HOW TO 메뉴 클릭
e = browser.find_element(By.LINK_TEXT, 'HOW TO')
e.click()

#4. 좌측 메뉴 중 Contact Form 메뉴 클릭
#e = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]')
#링크 텍스트 비교 > 'Contact Form'이라는 2개 이상의 링크 텍스트가 있는 경우 실패
#e = browser.find_element(By.LINK_TEXT, 'Contact Form') 
#일부 테스트 비교 방법
#e = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]')
#텍스트 전체 일치 비교
e = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]')
e.click()

#5. 입력란에 아래 값 입력
first_name = "길동"
last_name = "홍"
country = "Canada"
subject = "퀴즈 완료하였습니다."

e = browser.find_element(By.XPATH, '//*[@id="fname"]')
e.send_keys(first_name)

e = browser.find_element(By.XPATH, '//*[@id="lname"]')
e.send_keys(last_name)

e = browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(country))
e.click()

e = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea')
e.send_keys(subject)

#6. 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
e = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
e.click()

#7. 5초 대기 후 브라우저 종료
time.sleep(5)
browser.quit()


