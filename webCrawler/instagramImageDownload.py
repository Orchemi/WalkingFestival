from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# 태그 검색 후 이동할 웹 사이트 url
plusUrl = input('검색할 태그를 입력하세요 : ')
baseUrl = 'https://www.instagram.com/explore/tags/'


# 로그인 여부 확인
login_if = input('로그인을 하실건가요? (1)예 (2)아니오 : ')


# 로그인 하는 경우
if login_if == '1':
    # 로그인 화면에서 사용할 id/pw 계정
    id = input('계정을 입력하세요 : ')
    pw = input('비밀번호를 입력하세요 : ')

    # 크롬 드라이버 실행
    driver = webdriver.Chrome(
        executable_path='C:\Intellij\WalkingFestival\webCrawler\chromedriver.exe')
    # 상대경로를 사용하는 경우 에러가 발생하여, 절대경로를 입력

    # 인스타그램 로그인 화면으로 이동
    driver.get('https://www.instagram.com/accounts/login/')

    # drive.get(url) 이후에 창이 열릴 때까지 대기하는 시간 3초
    time.sleep(3)

    # 로그인 화면의 계정, 비밀번호 입력
    driver.find_element_by_name('username').send_keys(id)

    # input_id = driver.find_element_by_name('username')
    # input_id.send_keys(id)
    # 위 처럼 변수로 지정한 뒤 send_key를 따로 넣어도 됨.

    # driver.find_elements_by_class_name('_2hvTZ')[0].send_keys(id)도 가능
    # html 내에서 같은 클래스 명이 여러 개 있는 경우 indexing은 위와 같이 한다.

    driver.find_element_by_name('password').send_keys(pw)
    # driver.find_elements_by_class_name('_2hvTZ')[1].send_keys(pw)

    # ENTER 키 입력 방법
    e = driver.find_element_by_name('password')
    e.send_keys(Keys.ENTER)


# 로그인 하지 않는 경우
elif login_if == '2':

    # 크롬 드라이버 실행
    driver = webdriver.Chrome(
        executable_path='C:\Intellij\WalkingFestival\webCrawler\chromedriver.exe')

    # 인스타그램 로그인 화면으로 이동
    driver.get('https://www.instagram.com')

    # drive.get(url) 이후에 창이 열릴 때까지 대기하는 시간 2초
    time.sleep(2)


# 위에서 태그 입력에 대한 url 생성
url = baseUrl + quote_plus(plusUrl)
# 그냥 baseUrl + plusUrl 해버리면 input 그대로 들어가니까 plusUrl을 quote_plus 처리

driver.get(url)

time.sleep(10)

# 페이지 소스를 html 변수에 담음
html = driver.page_source

# 페이지 소스(html)을 bs 처리하여 soup 변수에 넣음
soup = BeautifulSoup(html)

# soup 변수에서 특정 클래스를 선택하여 insta 변수에 담음
insta = soup.select('.v1Nh3.kIKUG._bz0w')
# class 태그를 가져왔기 때문에 .을 찍는다.
# 3개의 클래스명이 있는 경우 공백을 없애고 모두 .을 찍는다.


# # 같은 클래스라면 다 가져오는 것
# print(insta)

# # insta의 클래스 중 하나만 가져오는 것
# print(insta[0])


n = 1   # 이미지 이름 생성 반복 처리를 위해 지정
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']

    with urlopen(imgUrl) as f:

        # 저장할 이미지 파일 이름
        saveimg = './img/' + plusUrl + str(n) + '.jpg'

        # 메모리의 이미지를 파일로 저장
        # text 가 아니라면 binary로 주어지기 때문에 wb(write binary) 사용
        with open(saveimg, 'wb') as h:
            img = f.read()
            h.write(img)
            h.close()
    n += 1


# 드라이버를 종료
driver.close()
