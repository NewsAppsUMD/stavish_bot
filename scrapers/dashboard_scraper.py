import requests
from bs4 import BeautifulSoup

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
print(html)

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('sr-only')

for row in table.find_all('data-modal'):
    print(row.prettify())
