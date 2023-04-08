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
        status = []
        status_p = div.find("p", {"data-issue-status": "icon"})
        status = [span.text.strip() for span in status_p.find_all("span")]
        update = []
        update_div = div.find("div", {"data-issue": "date"})
        update = [time.text.strip() for time in update_div.find_all("time")]
        #for update_div in div.find_all("div", {"data-issue": "date"}):
        #    updated.append(update.text.strip())
        actions = []
        for action in div.find_all("div", {"data-modal": "body"}):
            actions.append(action.text.strip())

        # Extract the text from the BeautifulSoup objects
        issues_text = ', '.join([issue.strip() for issue in issues])
        titles_text = ', '.join([title.strip() for title in titles])
        partners_div_text = ''
        if partners_div is not None:
            partners_div_text = ', '.join([li.text.strip() for li in partners_div.find_all("li")])
        #partners_li_text = ', '.join([li.text.strip() for li in partners_li])
        status_p_text = ''
        if status_p is not None:
            status_p_text = ', '.join([span.text.strip() for span in status_p.find_all("span")])
        #status_text = ', '.join([s.text.strip() for s in status])
        #status_span_text = ', '.join([sp.text.strip() for sp in status_span])
        update_div_text = ''
        if update_div is not None:
            update_div_text = ', '.join([time.text.strip() for time in update_div.find_all("time")])
        #updated_text = ', '.join([update.strip() for update in updated])
        actions_text = ', '.join([action.strip() for action in actions])

        # Write the extracted information to the CSV file
        writer.writerow([issues_text, titles_text, partners_div_text, status_p_text, update_div_text, actions_text])

print("Scraping complete.")










