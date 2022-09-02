import requests
from bs4 import BeautifulSoup as bs4
from selenium.webdriver import Chrome

from extractors.wwr import extract_wwr_jobs


# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
# url = "https://search.incruit.com/list/search.asp?col=all&src=gsw*www&kw="
# search_term = "python"
# response = requests.get(f"{url}{search_term}", headers=headers)
# response.raise_for_status()

browser = Chrome("/Users/csh/programming_language/001_Python/etc/nomad_coder_chellenge/chromedriver")
url = "https://www.indeed.com/jobs?q=python&limit=50"
browser.get(url)

# soup = bs4(response.text, "html.parser")
# job_list = soup.find("div", class_="cBbslist_contenst")
# jobs = job_list.find_all("ul")

# for job in jobs:
#     print(job)
#     print("="*50)
#     print("="*50)