#[네이버]-[네이버 항공권] 이번달 25일~26일 제주도 항공권 검색
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url='https://flight.naver.com'
browser.get(url)
time.sleep(2)

def wait_until(xpath):
    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))

#7일간 보지않기 버튼
btn = browser.find_element(By.CLASS_NAME, 'FullscreenPopup_suspend')
btn.click()
time.sleep(2)

#가는날선택
el = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
el.click()
time.sleep(2)

#이번달 25일
els = browser.find_elements(By.XPATH, '//b[text()="25"]')
els[0].click()
time.sleep(2)

#이번달 26일
els = browser.find_elements(By.XPATH, '//b[text()="26"]')
els[0].click()
time.sleep(2)

#도착
el = browser.find_element(By.XPATH, '//b[text()="도착"]')
el.click()
time.sleep(1)

#제주
el = browser.find_element(By.XPATH, '//button[text()="제주"]')
el.click()
time.sleep(1)

#항공권 검색
el = browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
el.click()
time.sleep(2)

try:
    with open('data/flight.txt', 'w', encoding='utf-8') as file:
        first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'
        wait_until(first)
        els = browser.find_elements(By.CLASS_NAME, 'domestic_Flight__8bR_b')
        for idx, el in enumerate(els):
            #print(f'[{idx}] {el.text}')
            #print('-' * 50)
            file.write(f'[{idx}] {el.text}\n')
            file.write('-' * 50)
            file.write('\n')
except:
    pass
finally:
    browser.quit()
    print('프로그램종료!')



