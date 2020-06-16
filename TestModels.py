#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import pickle
import random

from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import BernoulliNB, MultinomialNB

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from VoteClassifier import VoteClassifier

def load_youtube_comments():
    youtube_comments = open("Comments/youtube.txt", "r", encoding="utf8").read().split('\n')
    random.shuffle(youtube_comments)

    return youtube_comments

def load_tweets():
    tweets = open("Comments/tweets.txt", "r", encoding="utf8").read().split('\n')
    random.shuffle(tweets)

    return tweets

def load_content(path):
    text = open(path, "r", encoding="utf8").read().split('\n')
    random.shuffle(text)

    return text

def load_models():
    classifier = open(".\\pickled_algos\\NaiveBayes_customdataset.pickle", "rb")
    NB_NLTK = pickle.load(classifier)
    classifier.close()

    classifier = open(".\pickled_algos\Bernoulli_NB.pickle", "rb")
    Bernoulli_NB_Sklearn = pickle.load(classifier)
    classifier.close()

    classifier = open(".\pickled_algos\Multinomial_NB.pickle", "rb")
    Multi_NB_Sklearn = pickle.load(classifier)
    classifier.close()

    classifier = open(".\pickled_algos\LogisticRegression.pickle", "rb")
    LogReg = pickle.load(classifier)
    classifier.close()
    
    classifier = open(".\pickled_algos\Vectoriser.pickle", "rb")
    Vectoriser = pickle.load(classifier)
    classifier.close()

    return NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, LogReg, Vectoriser

def runModels(path):
    NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, LogReg, Vectoriser = load_models()
    voted_classifier = VoteClassifier(Vectoriser, NB_NLTK, Bernoulli_NB_Sklearn, LogReg, Multi_NB_Sklearn)
    content = load_content(path)
    print(f'First comment: {content[0]}')
    print(voted_classifier.classify(content))
    print(voted_classifier.confidence(content))

if __name__=="__main__":
    # Loading the models.
    NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, LogReg, Vectoriser = load_models()
    runModels("Comments/twitter.txt")

    
    # # Text to classify should be in a list.
    # text = ["I hate twitter"]
    '''
    youtube_comments = load_youtube_comments()
    print(f'\nYoutube comment:\n {youtube_comments[0]}')
    print('Multinomial Naive Bayes')
    predict(Vectoriser, Multi_NB_Sklearn, youtube_comments)
    print('Bernoulli Naive Bayes')
    predict(Vectoriser, Bernoulli_NB_Sklearn, youtube_comments)
    print('Naive Bayes NLTK')
    predict_NLTK(NB_NLTK, youtube_comments)

    tweets = load_tweets()
    print(f'\nTweet:\n {tweets[0]}')
    print('Multinomial Naive Bayes')
    predict(Vectoriser, Multi_NB_Sklearn, tweets)
    print('Bernoulli Naive Bayes')
    predict(Vectoriser, Bernoulli_NB_Sklearn, tweets)
    print('Naive Bayes NLTK')
    predict_NLTK(NB_NLTK, tweets)
    '''