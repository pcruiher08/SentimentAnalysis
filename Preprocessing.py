#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk import collocations
from nltk import ngrams
from langdetect import detect
import string

# Defining dictionary containing all emojis with their meanings.
emojis = {':)': 'smile', ':-)': 'smile', '8)':'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

def preprocess(textdata):
    stop_words = stopwords.words('english')
    
    # Defining regex patterns.
    urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern       = '@[^\s]+'
    alphaPattern      = "[^a-zA-Z0-9]"
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    
    tweets = []
    all_words_ngrams = []
    for tweet in textdata: 
        # Replace all URls with ''
        tweet = re.sub(urlPattern,'',tweet)
        # Replace all emojis.
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, '' + emojis[emoji])        
        # Replace @USERNAME to ''.
        tweet = re.sub(userPattern,'', tweet)        
        # Replace all non alphabets.
        tweet = re.sub(alphaPattern, ' ', tweet)
        # Replace 3 or more consecutive letters by 2 letter.
        tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
        tweet = tweet.strip()
        words_for_ngrams = []
        if len(tweet) > 1 and not tweet.isnumeric():    
           # if detect(tweet) == 'en': # Tarda demasiado y no mejora la deteccion de idioma; detecta igualmente el español
            tweet = word_tokenize(tweet)
            tweet, words_for_ngrams = clean_words(tweet,stop_words)
            tweets.append(tweet)
            all_words_ngrams.extend(words_for_ngrams)
        else:
            del tweet

    return tweets, all_words_ngrams

def bigrams(tweets_words,stop_words):
    bigrams_measures = collocations.BigramAssocMeasures()
    bigram_finder = collocations.BigramCollocationFinder.from_words(tweets_words)
    bigram_freq = bigram_finder.ngram_fd.items()
    
    bigramFreqTable = pd.DataFrame(list(bigram_freq), columns=['bigram','freq']).sort_values(by='freq', ascending=False)
    filtered_bi = bigramFreqTable[bigramFreqTable.bigram.map(lambda x: rightTypes(x,stop_words))]
    freq_bi = filtered_bi.bigram.values
    return freq_bi

def trigrams(tweets_words,stop_words):
    trigrams_measures = collocations.TrigramAssocMeasures()
    trigram_finder = collocations.TrigramCollocationFinder.from_words(tweets_words)
    trigram_freq = trigram_finder.ngram_fd.items()

    trigramFreqTable = pd.DataFrame(list(trigram_freq), columns=['trigram','freq']).sort_values(by='freq', ascending=False)
    filtered_tri = trigramFreqTable[trigramFreqTable.trigram.map(lambda x: rightTypesTri(x,stop_words))]
    freq_tri = filtered_tri.trigram.values
    return freq_tri

def rightTypes(ngram,stop_words):
    if '-pron-' in ngram or '' in ngram or ' 'in ngram or 't' in ngram:
        return False
    for word in ngram:
        if word in stop_words:
            return False
    acceptable_types = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    second_type = ('NN', 'NNS', 'NNP', 'NNPS')
    tags = nltk.pos_tag(ngram)
    if tags[0][1] in acceptable_types and tags[1][1] in second_type:
        return True
    else:
        return False

def rightTypesTri(ngram,stop_words):
    if '-pron-' in ngram or '' in ngram or ' 'in ngram or '  ' in ngram or 't' in ngram:
        return False
    for word in ngram:
        if word in stop_words:
            return False
    first_type = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    third_type = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    tags = nltk.pos_tag(ngram)
    if tags[0][1] in first_type and tags[2][1] in third_type:
        return True
    else:
        return False




important_words = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 
                   'such', 'no', 'nor', 'not', 'only', 'so', 'than', 'too', 
                   'very', 'just', 'but']

def clean_words(words, stop_words):
    words_clean = []
    ngrams_words_clean = []
    lemmatizer = WordNetLemmatizer()
    for word in words:
        word = word.lower()
        if word not in string.punctuation:
            word = lemmatizer.lemmatize(word)
            ngrams_words_clean.append(word)
            if word not in stop_words:
                words_clean.append(word)

    return words_clean, ngrams_words_clean

# for unigram
def bag_of_words(words):
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary

# for ngram (bigrams)
def bag_of_ngrams(words, n=2):
    words_ng = []
    for item in iter(ngrams(words,n)):
        words_ng.append(item)
    words_dictionary = dict([word, True] for word in words_ng)
    return words_dictionary

# Unigram an bigram
def bag_of_all_words(words, n=2):
    stopwords_english = stopwords.words('english')
    words_clean, _ = clean_words(words, stopwords_english)
    words_clean_brigram = clean_words(words, set(stopwords_english) - set(important_words))

    unigram_features = bag_of_words(words_clean)
    bigram_features = bag_of_ngrams(words_clean_brigram)

    all_features = unigram_features.copy()
    all_features.update(bigram_features)

    return all_features