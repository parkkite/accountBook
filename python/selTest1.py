from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Service 객체를 사용하여 ChromeDriver 경로 지정
service = Service('chromedriver.exe')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service)


# drive = webdriver.Chrome(executable_path="C:/chromedrive/chromedriver.chromedriver.exe")


driver.get('https://obank.kbstar.com/quics?page=C018897#idtabCont')
# driver.get('https://www.naver.com/')


r = driver.find_element(By.ID,'idtabCont')
time.sleep(10)
r.click()


id = driver.find_element(By.ID,'user_id')
id.send_keys('sdsd')

# # 로그인 절차
# driver.find_element(By.ID,'query').click

# setInput = driver.find_element_by_id("query")
# setInput = driver.find_element(By.ID,'query')
# setInput.send_keys("날씨")


# btn = driver.find_element(By.CLASS_NAME,'btn_search')
# btn.click()


# serInput = driver.find_element(By.CSS_SELECTOR('.search_input'))
# serInput.send_keys('날씨')

# btn = driver.find_element(By.CSS_SELECTOR('.btn_search'))
# btn.click

time.sleep(10)

driver.quit();


# username = driver.find_element_by_name('user_id')
# password = driver.find_element_by_name('user_pw')

# username.send_keys('A6206020')
# password.send_keys('A372137!')
# password.send_keys(Keys.RETURN)

# time.sleep(5)

# driver.get('https://obank.kbstar.com/quics?page=C102264&QSL=F')
# download_button = driver.find_element_by_xpath('//*[@id="excelDownload"]')
# download_button.click()




# time.sleep(1000)