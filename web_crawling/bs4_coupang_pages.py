import requests
import re
from bs4 import BeautifulSoup as bs4

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

for page in range(1,6):
    print("페이지 : ", page)

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:  # 원하는 조건에 해당하는 상품만 조회

        # 1. 광고 제품 제외
        ad_badge = re.search("search-product__ad-badge", str(item["class"]))
        if ad_badge:  # 광고 상품 제외
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
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:  # 평점 수 없는 상품 제외
            continue

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:  # 평점 4.5 이상, 평점 수 100개 이상

            price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격

            print(f"제품명 : {name}")
            print(f"가격   : {price}원")
            print(f"평점   : {rate}점({rate_cnt}개)")
            print("링크   : {}".format("https://www.coupang.com" + item.a["href"]))
            print()  # 가시성을 위해 제품과 제품 사이를 한 칸 띄움
