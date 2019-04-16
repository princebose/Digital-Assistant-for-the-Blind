import string
import speech
import google
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()

try:
    speech.say("A moment of silence, please.")
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        speech.say("Say something!")
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                speech.say("You said {}".format(value).encode("utf-8"))
                print("You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                speech.say("You said {}".format(value))
                print("You said {}".format(value))
            if value.lower() == "news":
                print "Which news headlines do you want to listen to? Say one for Times Or two CNN"
                speech.say("Which news headlines do you want to listen to? Say one for Times Or two CNN")
                with m as source: audio = r.listen(source)
                print("Got it! Now to recognize it...")
            # recognize speech using Google Speech Recognition
                news_sel = r.recognize_google(audio)
                speech.say("You chose %s" % news_sel)
                print "You chose {0}".format(news_sel)

                if ((news_sel.lower() == "one")or(news_sel.lower() == "1")or(news_sel.lower() == "times")or(news_sel.lower() == "games")or(news_sel.lower() == "x")):
                    url="http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
                    r= requests.get("http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms")
                    html_content = r.text
                    soup = BeautifulSoup(html_content, 'html.parser')
                    mylist1soup=soup.find_all('item')
                    i=1
                    for everytitle in mylist1soup:
                        print (everytitle.title.text)
                        speech.say(everytitle.title.text)

                if ((news_sel.lower() == "two")or(news_sel.lower() == "tu")or(news_sel.lower() == "2")or(news_sel.lower() == "cnn")):
                    url="http://rss.cnn.com/rss/edition.rss"
                    r= requests.get("http://rss.cnn.com/rss/edition.rss")
                    html_content = r.text
                    soup = BeautifulSoup(html_content, 'html.parser')
                    mylist1soup=soup.find_all('item')
                    i=1
                    for everytitle in mylist1soup:
                        print (everytitle.title.text)
                        speech.say(everytitle.title.text)


    #if value == "turn off":
            if value.lower() == "search":
                speech.say("What would you like to search for?")
                print("What would you like to search for?")
                with m as source: audio = r.listen(source)
                print("Got it! Now to recognize it...")
            # recognize speech using Google Speech Recognition
                query = r.recognize_google(audio)
                speech.say("Searching for %s" % query)
                print("Searching for %s" % query)

                for url in google.search(query, tld='com', lang='en', num=10, start=0, stop=20, pause=2.0):
                    print url
                    speech.say(url)


            if value.lower() == "goodbye":
                break


        except sr.UnknownValueError:
            speech.say("Oops! Didn't catch that")
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
