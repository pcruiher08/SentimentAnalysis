import nltk
import numpy as np
import random
import pickle
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
import string
#from nltk.corpus import wordnet

#To use NLTK with SkLearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode

'''
Combining Algorithms with NLTK to create our classifier
Combining classifier algorithms is is a common technique, done by creating a sort
 of voting system, where each algorithm gets one vote, and the classification that 
 has the most votes is the chosen one.
''' 

'''
Text classification
A fairly popular text classification task is to identify a body of text as either
spam or not spam, for things like email filters. In our case, we're going to try 
to create a sentiment analysis algorithm.
'''

'''
Naive Bayes will take every word in every review to find the most popular words used. 
Then, out of those most popular words we'll see which one appeared on positive
or negative connotations. Finally, we'll search for those words for whichever has
more positive or negative and that's how will classify.
'''

#List of tuples
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words_no_stopword = []
for word in movie_reviews.words():
    if word not in stopwords.words('english') and word not in string.punctuation:
        all_words_no_stopword.append(word.lower()) # lowercase

all_words_no_stopword = nltk.FreqDist(all_words_no_stopword)

word_features = [word[0] for word in all_words_no_stopword.most_common(3000)]

def find_features(document):
    words = set(document) #Avoid duplicates
    features = {}
    for word in word_features:
        features[word] = (word in words) #Boolean value if w in word_features is within the document
    return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(review), category) for (review,category) in documents]

training_set = featuresets[:1900]   # First 1900
testing_set = featuresets[1900:]    # Last 100

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = find_features(custom_review_tokens)
print (classifier.classify(custom_review_set))

custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = find_features(custom_review_tokens)
 
print (classifier.classify(custom_review_set))