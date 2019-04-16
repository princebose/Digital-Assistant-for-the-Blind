import string
import speech

while True:
    print "Talk:"
    value = speech.input()
    speech.say("You said %s" % value)
    print "You said {0}".format(value)
    #if value == "turn off":
    if value.lower() == "goodbye":
        break
