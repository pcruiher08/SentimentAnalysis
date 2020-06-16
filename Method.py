from twitter import Tweets
#from TestModels import runModels
from Youtube_scraper import Youtube

def call(method, counter):
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
    t = Youtube(list_terms)

def initVoice(counter):
    pass

def initInputFile(counter):
    fileName = input("Insert the filename: \n")
    #runModels(fileName)