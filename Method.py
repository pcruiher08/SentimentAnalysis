from twitter import Tweets
#from TestModels import runModels
from Youtube_scraper import Youtube

def call(method, counter):
    list_terms = getTerms()
    #select twitter, youtube, voice 
    switch = {
        'twitter' : initTwitter,
        'youtube' : initYoutube
    }

    methodCall = switch.get(method)
    methodCall(list_terms, counter)
    #runModels("Comments/" + method + ".txt")

def getTerms():
    x = input ("insert terms:")
    return x.split(' ')

def initTwitter(list_terms, counter):
    """ Init Twitter API with specified terms and counter """
    t = Tweets(list_terms, counter)

def initYoutube(list_terms, counter):
    print(list_terms)
    t = Youtube(list_terms)