import requests
from bs4 import BeautifulSoup

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
#heading = soup.find_all(id = "main")
#number = []
#for elem in heading:
  #finding the < a > tag
   #cards = elem.find_all("div")
#getting the text inside the < a > tag
#for i in cards:
  #number.append(i.string)
#print(number)
for i in soup.select('div.data-issue'):
    print(i.string)