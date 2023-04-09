import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from pprint import pprint
import csv
import os
import json
import smtplib
from email.mime.text import MIMEText
import hashlib

# website I'm scraping
url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# set file in an object
filename = "demandstable.csv"

# beautiful soup
soup = BeautifulSoup(response.content, "html.parser")

# define big div we working in 
divs = soup.find_all("div", {"data-card": "details"})

# organize columns of csv
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Issue', 'Title', 'Partner', 'Status', 'Updated', 'Actions'])

# loop through the html for each issue card on the website
    for div in divs:
        # issue loop
        issues = []
        for issue in div.find_all("p", {"data-issue-header": "index"}):
            issues.append(issue.text.strip())
        # title loop
        titles = []
        for title in div.find_all("h3", {"data-issue-header": "title"}):
            titles.append(title.text.strip())
        # partner loop
        partners = []
        partners_div = div.find("div", {"data-issue": "partners"})
        partners = [li.text.strip() for li in partners_div.find_all("li")]
        #status loop
        status = []
        status_p = div.find("p", {"data-issue-status": "icon"})
        status = [span.text.strip() for span in status_p.find_all("span")]
        # update loop
        update = []
        update_div = div.find("div", {"data-issue": "date"})
        update = [time.text.strip() for time in update_div.find_all("time")]
        # action loop
        actions = []
        action_umd_modal = div.find("div", {"data-modal": "body"})
        if action_umd_modal is not None:
            actions = [p.text.strip() for p in action_umd_modal.find_all("p")]

# now we joining our results and cutting it down so that we just get the text, not the html

        # issues join
        issues_text = ', '.join([issue.strip() for issue in issues])
        # titles join
        titles_text = ', '.join([title.strip() for title in titles])
        # partners join
        partners_div_text = ''
        if partners_div is not None:
            partners_div_text = ', '.join([li.text.strip() for li in partners_div.find_all("li")])
        # status join
        status_p_text = ''
        if status_p is not None:
            status_p_text = ', '.join([span.text.strip() for span in status_p.find_all("span")])
        # update join
        update_div_text = ''
        if update_div is not None:
            update_div_text = ', '.join([time.text.strip() for time in update_div.find_all("time")])
        # action join
        action_umd_modal_text = ', '.join([p.strip() for p in actions])
        if action_umd_modal is not None:
            action_umd_modal_text = ', '.join([p.text.strip() for p in action_umd_modal.find_all("p")])

# write it out to csv
        writer.writerow([issues_text, titles_text, partners_div_text, status_p_text, update_div_text, action_umd_modal_text])


def send_email(from_addr, to_addr, subject, body):
    # create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(Vstavish@gmail.com, os.environ['PASSWORD'])

    # check if changes were detected
    if len(changes) > 0:
        # add changes to body of email
        body += '\n\nChanges since last scrape:\n'
        for change in changes:
            body += change + '\n'

    # create message
    msg = MIMEText(body)
    msg['From'] = Vstavish@gmail.com
    msg['To'] = Vstavish@icloud.com
    msg['Subject'] = "25 demands update"

    # send message
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.quit()

print("Scraping complete.")












