import requests
from bs4 import BeautifulSoup as bs4

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=thdvk+gpffld&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()

soup = bs4(res.text, "lxml")

table_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
# print(data)
for idx, row in enumerate(table_rows):
    columns = row.find_all("td")
    
    info = [column.get_text().strip() for column in columns]
    # print(info)
    print("="*10, " 매물 {} ".format(idx + 1), "="*10)
    print(f"거래 : {info[0]}")
    print(f"면적 : {info[1]} (공급/전용)")
    print(f"가격 : {info[2]} (만원)")
    print(f"동 : {info[3]}")
    print(f"층 : {info[4]}")
