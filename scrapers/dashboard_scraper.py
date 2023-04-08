import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from pprint import pprint
import csv

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.content, "html.parser")

divs = soup.find_all("div", {"data-card": "details"})

# Loop through each div and extract the desired information
for div in divs:
    issue = soup.find_all("p", {"data-issue-header": "index"})
    title = soup.find_all("h3", {"data-issue-header": "title"})
    partners = soup.find_all("li")

print("Issue:", issue)
print("Title:", title)
print("Partners:", partners)







