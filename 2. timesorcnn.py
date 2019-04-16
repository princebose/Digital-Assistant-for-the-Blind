from bs4 import BeautifulSoup
import requests
myinput=input("enter your no.")
if myinput==1:
	url="http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
	r= requests.get("http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms")
	html_content = r.text
	soup = BeautifulSoup(html_content, 'html.parser')
	mylist1soup=soup.find_all('item')
	i=1
	for everytitle in mylist1soup:
		print '%2d '%i+(everytitle.title.text)
		i=i+1
elif myinput==2:
	url="http://rss.cnn.com/rss/edition.rss"
	r= requests.get("http://rss.cnn.com/rss/edition.rss")
	html_content = r.text
	soup = BeautifulSoup(html_content, 'html.parser')
	mylist1soup=soup.find_all('item')
	i=1
	for everytitle in mylist1soup:
		print '%2d '%i+(everytitle.title.text)
		i=i+1
else:
	print("enter valid input")
