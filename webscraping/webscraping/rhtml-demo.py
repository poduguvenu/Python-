from requests_html import HTML, HTMLSession
import csv

with open('sample.html') as html_file:
  source = html_file.read()
  html = HTML(html=source)
  html.render()

match = html.find('#footer', first=True)
print(match.text)

# articles = html.find('div.article')
# for article in articles:
#   headline = article.find('h2', first=True).text
#   summary = article.find('p', first=True).text
#   print(headline)
#   print(summary)



# csv_file = open('cms_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video'])



# session = HTMLSession()
# r = session.get('https://coreyms.com/')

# for link in r.html.absolute_links:
#   print(link)



# article = r.html.find('article', first=True)
# # print(article.html)
# headline = article.find('.entry-title-link', first=True).text
# # print(headline)

# summary = article.find('.entry-content p', first=True).text
# # print(summary)

# video_src = article.find('iframe', first=True).attrs['src']
# video_id = video_src.split('/')[4]
# video_id = video_id.split('?')[0]

# youtube_link = f'https://youtube.com/watch?v={video_id}'
# print(youtube_link)



# articles = r.html.find('article')

# for article in articles:
#   headline = article.find('.entry-title-link', first=True).text
#   print(headline)

#   summary = article.find('.entry-content p', first=True).text
#   print(summary)

#   try: 
#     video_src = article.find('iframe', first=True).attrs['src']
#     video_id = video_src.split('/')[4]
#     video_id = video_id.split('?')[0]
#   except Exception as e:
#     youtube_link = None

#   youtube_link = f'https://youtube.com/watch?v={video_id}'
#   print(youtube_link,'\n')

#   csv_writer.writerow([headline, summary, youtube_link])
# csv_file.close()


