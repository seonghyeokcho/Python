from selenium.webdriver import Chrome
from bs4 import BeautifulSoup as bs4
import time

browser = Chrome("/Users/csh/jupytercreation/Python_Practice/webcrawling/chromedriver")
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

## javaschript
# 지정한 스크롤 내리기(해상도 높이인 1200 위치로 스크롤 내리기)
# browser.execute_script("window.scrollTo(0, 1800)")  # 2880 x 1800
# browser.execute_script("window.scrollTo(0, 2800)")

# 스크롤 동작 대기시간
interval = 2

# 처음 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 스크롤 내리기 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기(위에서 설정한 interval 만큼)
    time.sleep(interval)

    # 스크롤을 내린 후의 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 이전 문서 높이와 현재 문서 높이를 비교하여 더이상 스크롤이 안될 시 멈춤
    if prev_height == curr_height:
        break
    # 이전 문서 높이와 현재 문서 높이가 같이 않다면 현재 문서 높이로 최신화
    prev_height = curr_height

# print("스크롤 완료!")

# 스크롤 내리기가 종료된 후 페이지상의 소스를 모두 가져옴
soup = bs4(browser.page_source, "lxml")
# list 형식으로 감싸줌으로써 "ImZGtf mpg5gc" class 를 가진 div, "Vpfmgd" class 를 가진 div 모두를 가져옴
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
# print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할일 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    # 할인 전 가격이 있다면 가격 정보를 저장
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    discounted_price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 할인된 영화 링크 정보
    # 가져온 a 객체의 href 속성은 "https://play.google.com" 가 제외된 주소라 올바른 주소가 아니므로 추가해줘야 함
    discounted_movie_link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})["href"]
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {discounted_price}")
    print(f"영화 링크 : {discounted_movie_link}")
    print("-"*120)

browser.quit()