import requests
from bs4 import BeautifulSoup

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
heading = soup.find(id = "main")
print(heading)
