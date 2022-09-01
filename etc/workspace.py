import requests
from bs4 import BeautifulSoup as bs4


headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = requests.get(f"{base_url}{search_term}", headers=headers)
response.raise_for_status()

soup = bs4(response.text, "html.parser")
jobs = soup.find_all("section", class_="jobs")

for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop()
    for post in job_posts:
        print(post)
        print("/"*20)