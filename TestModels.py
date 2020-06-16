#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import pickle
import random
from nltk.tokenize import word_tokenize
from Preprocessing import bag_of_all_words, preprocess

from sklearn.naive_bayes import BernoulliNB, MultinomialNB

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

def load_text():
    youtube_comments = open("Comments/Starlink.txt", "r").read().split('\n')
    random.shuffle(youtube_comments)
    youtube_comments.close()

    return  youtube_comments

def load_models():
    classifier = open("./pickled_algos/NaiveBayes_customdataset.pickle", "rb")
    NB_NLTK = pickle.load(classifier)
    classifier.close()

    classifier = open(".\pickled_algos\Bernoulli_NB.pickle", "rb")
    Bernoulli_NB_Sklearn = pickle.load(classifier)
    classifier.close()

    classifier = open(".\pickled_algos\Multinomial_NB.pickle", "rb")
    Multi_NB_Sklearn = pickle.load(classifier)
    classifier.close()
    
    classifier = open(".\pickled_algos\Vectoriser.pickle", "rb")
    Vectoriser = pickle.load(classifier)
    classifier.close()

    return NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, Vectoriser

def predict_NLTK(model, text):
    text = text[0]
    if len(text) > 1:
        print(type(text))
        print(text)
        custom_review_tokens = word_tokenize(text)
        print(custom_review_tokens)
        custom_review_set = bag_of_all_words(custom_review_tokens)

        print(model.classify(custom_review_set))
        prob_result = model.prob_classify(text[0])
        print (prob_result.prob("neg")) 
        print (prob_result.prob("pos")) 

def predict(vectoriser, model, text):
    # Predict the sentiment
    preprocessed_text = ' '
    preprocessed, _ = preprocess(text)
    preprocessed_text = ' '.join([str(word) for word in preprocessed[0]])
    textdata = vectoriser.transform(word_tokenize(preprocessed_text))
    prediction = model.predict(textdata)
    
    print(prediction[0])

if __name__=="__main__":
    # Loading the models.
    NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, Vectoriser = load_models()
    
    # Text to classify should be in a list.
    text = ["I hate twitter"]
    
    print('Multinomial Naive Bayes')
    predict(Vectoriser, Multi_NB_Sklearn, text)

    print('Bernoulli Naive Bayes')
    predict(Vectoriser, Bernoulli_NB_Sklearn, text)

    print('Naive Bayes NLTK')
    predict_NLTK(NB_NLTK, text)








# custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = bag_of_all_words(custom_review_tokens)
# print (classifier.classify(custom_review_set))
# # probability result
# prob_result = classifier.prob_classify(custom_review_set)
# # print (prob_result) 
# # print (prob_result.max()) 
# print (prob_result.prob("neg")) 
# print (prob_result.prob("pos")) 
# custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = bag_of_all_words(custom_review_tokens)
# print (classifier.classify(custom_review_set)) 
# prob_result = classifier.prob_classify(custom_review_set)
# # print (prob_result)
# # print (prob_result.max())
# print (prob_result.prob("neg")) 
# print (prob_result.prob("pos"))