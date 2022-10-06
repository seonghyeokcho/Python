from bs4 import BeautifulSoup as bs4
import requests

# How to open browser for selenium 4.x version
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    url = "https://kr.indeed.com/jobs?q="
    browser = Chrome(service=Service(ChromeDriverManager().install()), options=set_webdriver_options())
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


def set_webdriver_options():
    options = ChromeOptions()
    options.headless = True
    options.add_argument("window-size=2880x1800")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
    return options


def print_job_info(data):
    for k, v in data.items():
        print(f"{k}: {v}")
    print("="*30)

def extract_indeed_jobs(keyword):
    results = []
    
    pages = get_page_count(keyword)
    print(f"Found {pages} pages")
    
    for page in range(pages):
        url = "https://kr.indeed.com/jobs"
        final_url = f"{url}?q={keyword}&start={page*10}"
        print(f"Requesting {final_url}")
        
        # call Chrome browser
        browser = Chrome(service=Service(ChromeDriverManager().install()), options=set_webdriver_options())
        browser.get(final_url)
        
        # make beautiful soup
        soup = bs4(browser.page_source, "html.parser")
        
        # extract job data
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        print("="*30)
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
                    "company": company.string.replace(",", " "),
                    "location": location.string.replace(",", " "),
                    "position": title.replace(",", " "),
                }
                results.append(job_data)
                print_job_info(job_data)  # print job data
    return results

if __name__ == "__main__":
    term = input("What do you want search for?: ")
    extract_indeed_jobs(term)