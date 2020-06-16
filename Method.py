from twitter import Tweets
from TestModels import runModels
from Youtube_scraper import Youtube
import speech_recognition as sr

def initMethod(method, counter):
    #select twitter, youtube, voice, input file
    switch = {
        'twitter' : initTwitter,
        'youtube' : initYoutube,
        'voice'   : initVoice,
        'file'    : initInputFile
    }

    methodCall = switch.get(method)
    methodCall(counter)

def getTerms():
    x = input ("insert terms:")
    return x.split(' ')

def initTwitter(counter):
    """ Init Twitter API with specified terms and counter """
    t = Tweets(getTerms(), counter)
    #runModels("Comments/twitter.txt")

def initYoutube(counter):
    list_terms = getTerms()
    print(list_terms)
    t = Youtube(list_terms, counter)
    t.search_video()
    runModels("Comments/youtube.txt")

def initVoice(counter):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak Anything: ')
        audio = r.listen(source)
    try:
        t = r.recognize_google(audio)
        output = open('./Comments/voicetext.txt', 'w')
        output.write(t)
        output.close()
        # runModels("./Comments/voicetext.txt")
    except:
        print('Sorry could not recognize your voice')

def initInputFile(counter):
    fileName = input("Insert the filename: \n")
    #runModels(fileName)