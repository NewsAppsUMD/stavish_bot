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


my_data = []


html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('.data-issues-card')


for article in articles:


    title = article.select('.header')[0].get_text()
    excerpt = article.select('.small-san-serif')[0].get_text()
    pub_date = article.select('.extra-small-san-serif')[0].get_text()


    my_data.append({"title": title, "excerpt": excerpt, "pub_date": pub_date})


pprint(my_data)




