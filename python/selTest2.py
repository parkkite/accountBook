import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
from urllib.request import urlopen


# 크롬 드라이브 설정
service = Service('chromedriver.exe')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service)

# reqest로 통신하기
url = "https://openapi.openbanking.or.kr/v2.0/account/transaction_list/fin_num"

data = {"name": "John", "age": 30}
reps = requests.get(url,data=data)
print(reps.text)


# BeautifulSoup로 html 받아오기

url = urlopen('https://obank.kbstar.com/quics?page=C025255&cc=b028364:b028702&QSL=F#loading')
time.sleep(5)
url1 = BeautifulSoup(url,'html.parser')
vv = r.find('a',{'id':'idtabCont'})
print(vv)








