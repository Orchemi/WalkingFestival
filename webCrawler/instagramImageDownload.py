from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time


#
baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)
# 그냥 baseUrl + plusUrl 해버리면 input 그대로 들어가니까 plusUrl을 quote_plus 처리하여 넣는다.

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')
# class 태그를 가져왔기 때문에 .을 찍는다.
# 3개의 클래스명이 있는 경우 공백을 없애고 모두 .을 찍는다.

print(insta)

driver.close()
