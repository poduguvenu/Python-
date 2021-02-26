from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

# match = soup.title.text
# print(match)

# match = soup.find('div', class_='footer')
# print(match)

article = soup.find('div', class_='article')
# print(article)

headline = article.h2.a.text
# print(headline)

summary = article.p.text
# print(summary)

articles = soup.find_all('div', class_='article')
# print(articles)

for article in articles:
  headline = article.h2.a.text
  print(headline)
  summary = article.p.text
  print(summary)
  print()