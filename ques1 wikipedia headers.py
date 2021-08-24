# Python program to print all heading tags
import requests
from bs4 import BeautifulSoup
 
# scraping a wikipedia article
url_link = 'https://en.wikipedia.org/wiki/Main_Page'
request = requests.get(url_link)
 
Soup = BeautifulSoup(request.text, 'lxml')
 
# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in Soup.find_all(heading_tags):
    print(tags.name + ' -> ' + tags.text.strip())