#예보
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url='https://www.weather.go.kr/w/index.do'
browser.get(url)

#전국
el = browser.find_element(By.XPATH, '//a[text()="전국"]')
el.click()
time.sleep(1)

#예보
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]/a/span'
el = browser.find_element(By.XPATH, xpath)
el.click()
time.sleep(1)

for i in range(1, 8):
    xpath=f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
    el = browser.find_element(By.XPATH, xpath)
    title = el.text.replace('\n','')
    print(f'------------- {title}-----------------')
    el.click()
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source, 'lxml')
    local = soup.find('div', {'id':'weather'})
    els = local.find_all('dl', re.compile('^po_'))
    for el in els:
        name = el.dt.getText()
        temp = el.span.getText()
        weather = el.i.getText()
        print(name, temp, weather)