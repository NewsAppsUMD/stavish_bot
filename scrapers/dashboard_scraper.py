import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from pprint import pprint

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())






