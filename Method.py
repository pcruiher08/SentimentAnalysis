from twitter import Tweets

def call(method):
    list_terms = getTerms()
    #select twitter, youtube, voice 
    switch = {
        'twitter' : initTwitter,
        'youtube' : initYoutube
    }

    methodCall = switch.get(method)
    methodCall(list_terms)

def getTerms():
    x = input ("insert terms:")
    return x.split(' ')

def initTwitter(list_terms):
    print(list_terms)
    t = Tweets(list_terms)

def initYoutube(list_terms):
    pass
