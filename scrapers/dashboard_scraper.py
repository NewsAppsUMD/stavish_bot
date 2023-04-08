import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from pprint import pprint

url = 'https://diversity.umd.edu/black-student-leaders'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.content, "html.parser")

divs = soup.find_all("div", {"data-card": "details"})

# Loop through each div tag and extract the desired information
for div in divs:
    # Extract the title
    title = div.find("h3").text.strip()

    # Extract the description
    description = div.find("div", {"class": "desc"}).text.strip()

    # Extract the image URL
    img_url = div.find("img")["src"]

    # Print out the extracted information
    print("Title:", title)
    print("Description:", description)
    print("Image URL:", img_url)
    print("\n")







