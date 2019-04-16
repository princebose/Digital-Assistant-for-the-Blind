import string
import speech
from bs4 import BeautifulSoup
import requests
while True:
    print "Talk:"
    phrase = speech.input()
    speech.say("You said %s" % phrase)
    print "You said {0}".format(phrase)
    if phrase.lower() == "news":
        print "Which news headlines do you want to listen to? Times Or CNN"
        speech.say("Which news headlines do you want to listen to? Times Or CNN")
        news_sel = speech.input()
        speech.say("You chose %s" % news_sel)
        print "You chose {0}".format(news_sel)

        if news_sel.lower() == "times":
            url="http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
            r= requests.get("http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms")
            html_content = r.text
            soup = BeautifulSoup(html_content, 'html.parser')
            mylist1soup=soup.find_all('item')
            i=1
            for everytitle in mylist1soup:
                print (everytitle.title.text)
                speech.say(everytitle.title.text)

        if news_sel.lower() == "cnn":
            url="http://rss.cnn.com/rss/edition.rss"
            r= requests.get("http://rss.cnn.com/rss/edition.rss")
            html_content = r.text
            soup = BeautifulSoup(html_content, 'html.parser')
            mylist1soup=soup.find_all('item')
            i=1
            for everytitle in mylist1soup:
                print (everytitle.title.text)
                speech.say(everytitle.title.text)


    #if phrase == "turn off":
    if phrase.lower() == "goodbye":
        break
