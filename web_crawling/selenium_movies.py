import requests
from bs4 import BeautifulSoup as bs4

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf-8-sig") as f:
#     f.write(soup.prettify())  # html 문서를 예쁘게 출력해줌

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)