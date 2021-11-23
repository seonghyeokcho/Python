# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup as bs4

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = bs4(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)  # a element 의 속성 정보를 모두 출력
# print(soup.a['href'])  # a element 의 href 속성'값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # <a> 요소 중 클래스가 'Nbtn_upload' 에 해당하는 첫 번째 <a> 요소를 출력
# print(soup.find(attrs={"class":"Nbtn_upload"}))  # 클래스가 'Nbtn_upload' 인 어떤 요소 중 해당하는 첫 번째 요소를 출력

# print(soup.find("li", attrs={"class":'rank01'}))
rank1 = soup.find("li", attrs={"class":'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="싸움독학-102화 : 오늘은 좀 쓰네")
print(webtoon)