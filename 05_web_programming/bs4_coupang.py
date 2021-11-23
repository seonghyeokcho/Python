import requests
import re
from bs4 import BeautifulSoup as bs4

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs4(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:  # 원하는 조건에 해당하는 상품만 조회

    # 1. 광고 제품 제외
    ad_badge = re.search("search-product__ad-badge", str(item["class"]))
    if ad_badge:  # 광고 상품 제외
        # print("<광고 상품>")
        # kind_of_badge = item.find("div", attrs={"class":"badges"})
        # if kind_of_badge.get_text() == " ":
        #     print("광고 종류 : ", "쿠팡 추천")
        #     print("링크      : ", "https://www.coupang.com" + item.a["href"])
        #     print()
        #     continue
        # print("광고 종류 : ", kind_of_badge.get_text())
        # print("링크      : ", "https://www.coupang.com" + item.a["href"])
        # print()
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명

    # 2. 특정 제품 제외
    if "Apple" in name:  # Apple 상품 제외
        continue

    # 3. 평점 4.5 이상, 평점 수 100개 이상만 조회
    rate = item.find("em", attrs={"class":"rating"})  # 평점

    if rate:
        rate = rate.get_text()
    else:  # 평점 없는 상품 제외
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수

    if rate_cnt:
        rate_cnt = rate_cnt.get_text()[1:-1]  # 숫자 이외에 문자열이 포함되어 있음 {ex : (26)}
        # [1:-1] : 숫자만 가져옴 (ex : (26) -> 0번째 index : (, 1번째 index : 2, 2번째 index : 6, 3번째 index : ) 중 1번째부터 -2 까지 즉, 끝에서 2번째까지만 포함)
    else:  # 평점 수 없는 상품 제외
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:  # 평점 4.5 이상, 평점 수 100개 이상

        price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격

        print("제품명 : ", name)
        print("가격   : ", price + "원")
        print("평점   : ", rate + "점")
        print("평점수 : ", rate_cnt + "개")
        print("링크   : ", "https://www.coupang.com" + item.a["href"])
        print()  # 가시성을 위해 제품과 제품 사이를 한 칸 띄움
