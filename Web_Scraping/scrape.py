import requests
import lxml
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)
quotes = soup.find_all('span', class_='text')
author = soup.find_all('small',class_='author')
tags = soup.find_all('div', class_='tags')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(author[i].text)
    quotetags = tags[i].find_all('a',class_='tag')
    for quotetag in quotetags:
        print(quotetag.text)

### Refer scrapingclub.com for more exercises on web scraping use cases




