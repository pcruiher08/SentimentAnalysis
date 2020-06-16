import re
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from Preprocessing import bag_of_all_words, preprocess
from statistics import mode #for the votes
import vader

class VoteClassifier(ClassifierI):
    def __init__(self, vectoriser, *classifiers):
        self._classifiers = classifiers
        self._SKLearnVectoriser = vectoriser
        
    def predict_NLTK(self, model, text):
        custom_review_tokens = word_tokenize(text)
        custom_review_set = bag_of_all_words(custom_review_tokens)
        return  model.classify(custom_review_set)

    def predict_SKLearn(self, vectoriser, model, text):
        # Predict the sentiment
        preprocessed_text = ' '
        preprocessed, _ = preprocess([text])
        preprocessed_text = ' '.join([str(word) for word in preprocessed])
        textdata = vectoriser.transform(word_tokenize(preprocessed_text))
        prediction = model.predict(textdata)
        return prediction[0]

    def classify(self, comment):
        votes = []
        for model in self._classifiers:
            if re.search('sklearn+',str(type(model))):
                v = self.predict_SKLearn(self._SKLearnVectoriser, model, comment)
                votes.append(v)
            else:
                v = self.predict_NLTK(model, comment)
                votes.append(v)
        votes.append(vader.analyze(comment)[0])
        return mode(votes)
        
    def confidence(self, comment):
        votes = []
        for model in self._classifiers:
            if re.search('sklearn+',str(type(model))):
                v = self.predict_SKLearn(self._SKLearnVectoriser, model, comment)
                votes.append(v)
            else:
                v = self.predict_NLTK(model, comment)
                votes.append(v)
        votes.append(vader.analyze(comment)[1])
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf