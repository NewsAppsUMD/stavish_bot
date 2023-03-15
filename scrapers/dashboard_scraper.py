import requests
from bs4 import BeautifulSoup

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
heading = soup.find_all(id = "main")
names = []
for elem in heading:
  #finding the < a > tag
cards = elem.find_all("data-issues-cards")
#getting the text inside the < a > tag
for i in cards:
  names.append(i.string)
print(names)