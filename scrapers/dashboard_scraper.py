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

with open('25_demands_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Issue', 'Title', 'Partner', 'Status', 'Updated', 'Actions'])

    for div in divs:
        issues = []
        for issue in div.find_all("p", {"data-issue-header": "index"}):
            issues.append(issue.text.strip())
        titles = []
        for title in div.find_all("h3", {"data-issue-header": "title"}):
            titles.append(title.text.strip())
        partners = []
        partners_div = div.find("div", {"data-issue": "partners"})
            partners = [li.text.strip() for li in partners_div.find_all("li")]
        #this status one needs help
        status = soup.find_all("p", {"data-issue-status": "icon"})
        status_span = soup.find_all("span")
        updated = []
        for update in div.find_all("div", {"data-issue": "date"}):
            updated.append(update.text.strip())
        actions = []
        for action in div.find_all("div", {"data-modal": "body"}):
            actions.append(action.text.strip())

        # Extract the text from the BeautifulSoup objects
        issues_text = ', '.join([issue.strip() for issue in issues])
        titles_text = ', '.join([title.strip() for title in titles])
        partners_li_text = ', '.join([partners_li.strip() for partner in partners])
        #partners_li_text = ', '.join([li.text.strip() for li in partners_li])
        status_text = ', '.join([s.text.strip() for s in status])
        status_span_text = ', '.join([sp.text.strip() for sp in status_span])
        updated_text = ', '.join([update.strip() for update in updated])
        actions_text = ', '.join([action.strip() for action in actions])

        # Write the extracted information to the CSV file
        writer.writerow([issues_text, titles_text, partners_li_text, status_text, updated_text, actions_text])

print("Scraping complete.")










