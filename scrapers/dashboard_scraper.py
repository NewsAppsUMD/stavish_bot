import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

data = requests.get(url)

html = BeautifulSoup(data.text, 'html.parser')

datas = soup.find_all("details")

# Iterate through all li tags
for data in datas:
    # Get text from each tag
    print(data.text)
 
print(f"Total {len(datas)} li tag found")






