import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
res = requests.get(url, headers=headers)  # user agent 를 넣어 줌으로써 실제 크롬에서 접속했을때와 동일한 결과를 받아 옴
res.raise_for_status()

with open("Python_Practice/webcrawling/webscraping_basic/nadocoding.html", 'w', encoding='utf8') as f:
    f.write(res.text)