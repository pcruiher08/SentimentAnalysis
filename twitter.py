'''
Created on June 09, 2020
@author: Mildred Gil Melchor
'''
import pymongo
from pymongo import MongoClient
from pprint import pprint
import sys
from config import *
import tweepy
import preprocessor as p
from langdetect import detect

class Tweets( ):
    def __init__(self, terms):
        '''
        OAUTH
        '''
        CONSUMER_KEY      = keys["ckey"]
        CONSUMER_SECRET   = keys["csecret"]
        OAUTH_TOKEN       = keys["atoken"]
        OATH_TOKEN_SECRET = keys["asecret"]

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OATH_TOKEN_SECRET)

        api = tweepy.API(auth)
        
        myStreamListener = MyStreamListener()   
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=terms) #myStream.filter(track=track, is_async=True)

def isEnglish(sentence):
    return detect(sentence) == 'en'

class MyStreamListener(tweepy.StreamListener):
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_status(self, status):
        try:
            print( status._json["text"] )
            clean_text = p.clean( status._json["text"] )

            if isEnglish ( clean_text ):
                output = open("tweets.txt","a")
                output.write(clean_text)
                output.write('\n')
                output.close()
        except:
            pass
   
    def on_error(self, status_code):
        if status_code == 420:
            return False