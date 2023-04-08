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
    partners = soup.find_all("div", {"data-issue": "partners"})
    partners_li = soup.find_all("ul")
    #this status one needs help
    status = soup.find_all("p", {"data-issue-status": "icon"})
    status_span = soup.find_all("span")
    updated = soup.find_all("div", {"data-issue": "date"})
    actions = soup.find_all("div", {"data-modal": "body"}).text.strip()

issue_text = issue.get_text()

print("Issue:", issue_text)
print("Title:", title)
print("Partners:", partners_li)
print("Status:", status_span)
print("Updated:", updated)
print("Actions:", actions)







