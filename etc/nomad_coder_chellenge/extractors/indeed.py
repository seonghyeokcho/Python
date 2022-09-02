from bs4 import BeautifulSoup as bs4
import requests

# How to open browser for selenium 4.x version
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    url = "https://kr.indeed.com/jobs?q="
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(f"{url}{keyword}")
    soup = bs4(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    
    if pagination == None:
        return 1
    
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    results = []
    pages = get_page_count(keyword)
    print(f"Found {pages} pages")
    
    for page in range(pages):
        url = "https://kr.indeed.com/jobs"
        final_url = f"{url}?q={keyword}&start={page*10}"
        print(f"Requesting {final_url}")
        browser = Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(final_url)
        soup = bs4(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)

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
    return results