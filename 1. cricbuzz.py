from bs4 import BeautifulSoup
import requests
url="http://live-feeds.cricbuzz.com/CricbuzzFeed"
r= requests.get("http://live-feeds.cricbuzz.com/CricbuzzFeed")
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')
i=1
mylist1soup=soup.find_all('item')
for everytitle in mylist1soup:	
		print '%2d '%i+(everytitle.title.text)
		soup=(everytitle.description.text).split('<div')[0]
		print soup
		i=i+1
