from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #브라우저창이 항상 오픈
brower = webdriver.Chrome(options=options)

brower.maximize_window()

url = 'https://flight.naver.com'
brower.get(url)

brower.get_screenshot_as_file('data/flight.png') #화면을 캡쳐해서 파일로 저장
brower.quit()