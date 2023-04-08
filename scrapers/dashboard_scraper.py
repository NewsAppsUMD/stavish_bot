import requests
from bs4 import BeautifulSoup
import time
import urllib.request

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
print(html)

# Set the URL of the website you want to check
url = 'https://diversity.umd.edu/black-student-leaders'


# Use requests to get the HTML content of the website
response = requests.get(url)


# Open a file in write mode and save the content as text
with open('25_demands_dashboard.txt', 'w') as f:
    f.write(response.text)


# Set the name of the file to store the previous content
previous_content_file = '25_demands_dashboard.txt'


# Try to open the file and read the previous content
try:
    with open(previous_content_file, 'r') as f:
        previous_content = f.read()
except:
    previous_content = ''


# Get the current content of the website
current_content = response.text


# Use difflib to compare the current content to the previous content
d = difflib.Differ()
diff = list(d.compare(previous_content.splitlines(), current_content.splitlines()))


# Print the differences
if diff:
    print('Website updated:')
    for line in diff:
        if line.startswith('+') or line.startswith('-'):
            print(line)
else:
    print('No updates')
