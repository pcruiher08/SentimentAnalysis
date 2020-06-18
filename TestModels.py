import nltk
import pickle
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from VoteClassifier import VoteClassifier

def load_content(path):
    """ Return the tweets, comment or voice input text from their \n
        respective file.
    """
    text = open(path, "r").read().split('\n')
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
    """ Init vote Classifier with the models and analyze each comment \n
        saving the sentiment value (pos or neg) into the result file.
    """
    NB_NLTK, Bernoulli_NB_Sklearn, Multi_NB_Sklearn, LogReg, Vectoriser = load_models()
    voted_classifier = VoteClassifier(Vectoriser, NB_NLTK, Bernoulli_NB_Sklearn, LogReg, Multi_NB_Sklearn)
    content = load_content(path)
    
    #clean file
    output = open("results.txt","w")
    output.write('')
    output.close()

    for sentence in content:
        if len(sentence) > 1:
            sentiment_value, confidence = sentiment(sentence, voted_classifier)

            # Accept only the sentiment values with a confidence higher than .7
            if confidence* 100 > 70:
                output = open("results.txt","a")
                output.write(sentiment_value + ' : ')
                output.write(sentence)
                output.write('\n')
                output.close()

def sentiment(sentence, voted_classifier):
    return voted_classifier.classify(sentence), voted_classifier.confidence(sentence)
