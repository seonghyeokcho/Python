import requests
from bs4 import BeautifulSoup as bs4

from extractors.wwr import extract_wwr_jobs


jobs = extract_wwr_jobs("python")
print(jobs)