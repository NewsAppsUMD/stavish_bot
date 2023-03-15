import requests
from bs4 import BeautifulSoup

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('h3.small.san.serif')
print(table.prettify())
