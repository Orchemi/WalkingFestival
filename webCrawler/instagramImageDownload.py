from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

id = input('계정을 입력하세요 : ')
pw = input('비밀번호를 입력하세요 : ')

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')

url = baseUrl + quote_plus(plusUrl)
# 그냥 baseUrl + plusUrl 해버리면 input 그대로 들어가니까 plusUrl을 quote_plus 처리하여 넣는다.

# 상대경로를 사용한 경우 에러가 발생하여, 절대경로를 입력
driver = webdriver.Chrome(
    executable_path='C:\Intellij\WalkingFestival\webCrawler\chromedriver.exe')

driver.get(url)

time.sleep(5)
# drive.get(url) 이후에 창이 열릴 때까지 대기하는 시간 5초

# html = driver.page_source
# soup = BeautifulSoup(html)


# insta = soup.select('.v1Nh3.kIKUG._bz0w')
# # class 태그를 가져왔기 때문에 .을 찍는다.
# # 3개의 클래스명이 있는 경우 공백을 없애고 모두 .을 찍는다.


# # print(insta)
# # 같은 클래스라면 다 가져오는 것

# # print(insta[0])
# # insta의 클래스 중 하나만 가져오는 것


# for i in insta:
#     print('https://www.instagram.com' + i.a['href'])

# driver.close()
# # 드라이버를 닫아준다.
