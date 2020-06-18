#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import random
import pickle
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from nltk import ngrams
import string

""" This is the script in which the training of NLTK Naive Bayes was done"""

""" Important words to ignore when removing stop words """
important_words = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 
                   'such', 'no', 'nor', 'not', 'only', 'so', 'than', 'too', 
                   'very', 'just', 'but']

# Comment when not using the next dataset
# 5532 reviews each file
short_pos = open("reviews/positive.txt", encoding='latin-1').read()
short_neg = open("reviews/negative.txt", encoding='latin-1').read()

def clean_words(words, stopwords_language):
    """ Removes stop words, string punctuations and puts in lowercase the words """
    words_clean = []
    for word in words:
        word = word.lower()
        if word not in stopwords_language and word not in string.punctuation:
            words_clean.append(word)
    return words_clean

def bag_of_words(words):
    """ Returns a vector of binary features for unigrams """
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary

def bag_of_ngrams(words, n=2):
    """ Returns a vector of binary features for bigrams """
    words_ng = []
    for item in iter(ngrams(words,n)):
        words_ng.append(item)
    words_dictionary = dict([word, True] for word in words_ng)
    #print(words_dictionary)
    return words_dictionary

def bag_of_all_words(words, n=2):
    """ Returns a vector of binary features for unigrams and bigrams """
    stopwords_english = stopwords.words('english')
    words_clean = clean_words(words, stopwords_english)
    words_clean_brigram = clean_words(words, set(stopwords_english) - set(important_words))

    unigram_features = bag_of_words(words_clean)
    bigram_features = bag_of_ngrams(words_clean_brigram)

    all_features = unigram_features.copy()
    all_features.update(bigram_features)

    return all_features

""" Preprocess the dataset """
pos_reviews = []
# for fileid in movie_reviews.fileids('pos'):
#     pos_reviews.append(movie_reviews.words(fileid))
for pos_review in short_pos.split('\n'):
    pos_reviews.append(word_tokenize(pos_review)) 

neg_reviews = []
# for fileid in movie_reviews.fileids('neg'):
#     neg_reviews.append(movie_reviews.words(fileid))
for neg_review in short_neg.split('\n'):
    neg_reviews.append(word_tokenize(neg_review)) 

pos_review_set = []
for words in pos_reviews:
    pos_review_set.append((bag_of_all_words(words), 'pos'))

neg_review_set = []
for words in neg_reviews:
    neg_review_set.append((bag_of_all_words(words), 'neg'))

random.shuffle(pos_review_set)
random.shuffle(neg_review_set)

""" Train the classifier """
test_set = pos_review_set[:1066] + neg_review_set[:1066]
train_set = pos_review_set[1066:] + neg_review_set[1066:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.accuracy(classifier,test_set)
print(accuracy)
print(classifier.show_most_informative_features(15))

""" Save the classifier """
save_classifier = open("pickled_algos/NaiveBayes_customdataset.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


'''
Notes:

Combining Algorithms with NLTK to create our classifier
Combining classifier algorithms is is a common technique, done by creating a sort
of voting system, where each algorithm gets one vote, and the classification that 
has the most votes is the chosen one.
Text classification
A fairly popular text classification task is to identify a body of text as either
spam or not spam, for things like email filters. In our case, we're going to try 
to create a sentiment analysis algorithm.
Naive Bayes will take every word in every review to find the most popular words used. 
Then, out of those most popular words we'll see which one appeared on positive
or negative connotations. Finally, we'll search for those words for whichever has
more positive or negative and that's how will classify.
CUSTOM DATASET GIVES BETTER PREDICTIONS RATHER THAN USING THE MOVIEW REVIEWS
'''

# Bag on NGrams feature
# From: http://blog.chapagain.com.np/python-nltk-sentiment-analysis-on-movie-reviews-natural-language-processing-nlp/