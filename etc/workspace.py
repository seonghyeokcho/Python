import requests
from bs4 import BeautifulSoup as bs4


headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

websites = [
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com"
]

for website in websites:
    if not website.startswith("http://"):
        website = f"http://{website}"
    # result = requests.get(website)
    # result.raise_for_status()
    print(website)
    
    