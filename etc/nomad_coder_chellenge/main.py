from bs4 import BeautifulSoup as bs4

# How to open browser for selenium 4.x version
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from extractors.wwr import extract_wwr_jobs


url = "https://kr.indeed.com/jobs?q="
search_term = "python"
browser = Chrome(service=Service(ChromeDriverManager().install()))
browser.get(f"{url}{search_term}")

soup = bs4(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
results = []

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "link": f"https://kr.indeed.com{link}",
            "company": company.string,
            "location": location.string,
            "position": title
        }
        results.append(job_data)

for result in results:
    print(result)
    print("="*30)
    print("="*30)