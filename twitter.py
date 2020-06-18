'''
Created on June 09, 2020
@author: Mildred Gil Melchor
'''
from pprint import pprint
import sys
from config import *
import tweepy
import preprocessor as p
from langdetect import detect

class Tweets( ):
    """ Handles the Twitter API. """
    
    def __init__(self, terms, counter):
        """ Inits API keys and the Stream Listener."""
        
        CONSUMER_KEY      = keys["ckey"]
        CONSUMER_SECRET   = keys["csecret"]
        OAUTH_TOKEN       = keys["atoken"]
        OATH_TOKEN_SECRET = keys["asecret"]

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OATH_TOKEN_SECRET)

        api = tweepy.API(auth)
        
        myStreamListener = MyStreamListener(num_tweets_to_grab=counter)
        myStream         = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=terms)

def isEnglish(sentence):
    return detect(sentence) == 'en'

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, num_tweets_to_grab, api=None):
        super(MyStreamListener, self).__init__()

        #clean file
        output = open("Comments/twitter.txt","w")
        output.write('')
        output.close()

        self.counter = 0
        self.num_tweets_to_grab = num_tweets_to_grab

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_status(self, status):
        if self.counter > self.num_tweets_to_grab:
            return False

        try:
            # Clean tweets from emojis, urls, and special characters
            clean_text = p.clean( status._json["text"] )

            # Accept only english tweets
            if isEnglish ( clean_text ):
                output = open("Comments/twitter.txt","a")
                output.write(clean_text)
                output.write('\n')
                output.close()
                self.counter += 1
        except:
            pass
   
    def on_error(self, status_code):
        if status_code == 420:
            return False