import requests
from bs4 import BeautifulSoup

#Scrap the given website for quotes
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

#Find the elements
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

#Loop over the quotes
#Print the quote, author, and quote tags
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

#Run py scrape.py in the terminal (Windows)