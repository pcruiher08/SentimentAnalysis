from twitter import Tweets
from TestModels import runModels

def call(method):
    list_terms = getTerms()
    #select twitter, youtube, voice 
    switch = {
        'twitter' : initTwitter,
        'youtube' : initYoutube
    }

    methodCall = switch.get(method)
    methodCall(list_terms)
    runModels("Comments/" + method + ".txt")

def getTerms():
    x = input ("insert terms:")
    return x.split(' ')

def initTwitter(list_terms):
     """ Init Twitter API with specified terms. """
    t = Tweets(list_terms)

def initYoutube(list_terms):
    pass
