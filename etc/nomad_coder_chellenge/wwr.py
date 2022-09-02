import requests
from bs4 import BeautifulSoup as bs4


headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = requests.get(f"{base_url}{search_term}", headers=headers)
response.raise_for_status()

results = []
soup = bs4(response.text, "html.parser")
jobs = soup.find_all("section", class_="jobs")

for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop()
    for post in job_posts:
        anchor = post.find_all("a")[1]
        link = anchor["href"]
        company, _, region = anchor.find_all("span", class_="company")
        title = anchor.find("span", class_="title")
        # print(company.string, region.string, title.string)
        job_data = {
            "company": company.string,
            "region": region.string,
            "position": title.string,
            "link": f"https://weworkremotely.com{link}"
        }
        results.append(job_data)
        
print("="*60)
for result in results:
    print(result)
    print("="*30)