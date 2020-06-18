from twitter import Tweets
from TestModels import runModels
from Youtube_scraper import Youtube
import speech_recognition as sr

def initMethod(method, counter):
    """ Select twitter, youtube, voice, input file, and init."""
    switch = {
        'twitter' : initTwitter,
        'youtube' : initYoutube,
        'voice'   : initVoice,
        'file'    : initInputFile
    }

    methodCall = switch.get(method)
    methodCall(counter)

def getTerms():
    """ Ask the user to insert the terms of interest. """
    x = input ("insert terms:")
    return x.split(' ')

def initTwitter(counter):
    """ Initialize Twitter API with specified terms and counter. """
    t = Tweets(getTerms(), counter)
    runModels("Comments/twitter.txt")

def initYoutube(counter):
    """ Initialize youtube scrapper. """
    list_terms = getTerms()
    print(list_terms)
    t = Youtube(list_terms, counter)
    t.search_video()
    runModels("Comments/youtube.txt")

def initVoice(counter):
    """ Initialize the voice system and save it into a file """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak Anything: ')
        audio = r.listen(source)
    try:
        t = r.recognize_google(audio)
        output = open('./Comments/voicetext.txt', 'w')
        output.write(t)
        output.close()
        print(t)
        runModels("./Comments/voicetext.txt")
    except:
        print('Sorry could not recognize your voice')

def initInputFile(counter):
    fileName = input("Insert the filename: \n")
    runModels(fileName)