import re
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from Preprocessing import bag_of_all_words, preprocess
from statistics import mode #for the votes

class VoteClassifier(ClassifierI):
    def __init__(self, vectoriser, *classifiers):
        self._classifiers = classifiers
        self._SKLearnVectoriser = vectoriser
        
    def predict_NLTK(self, model, text):
        if len(text) > 1:
            custom_review_tokens = word_tokenize(text)
            custom_review_set = bag_of_all_words(custom_review_tokens)
            return  model.classify(custom_review_set)

        # with open(absolute_test_dir + to_search + '.txt', 'w') as f:
        #     comments = clean_comments(comments)
        #     for cmt in range(desired_comments):
        #         comment = comments[cmt]
        #         f.write(comment + '\n')


    def predict_SKLearn(self, vectoriser, model, text):
        # Predict the sentiment
        preprocessed_text = ' '
        preprocessed, _ = preprocess(text)
        preprocessed_text = ' '.join([str(word) for word in preprocessed[0]])
        textdata = vectoriser.transform(word_tokenize(preprocessed_text))
        prediction = model.predict(textdata)
        return prediction[0]

    def classify(self, features):
        votes = []
        for model in self._classifiers:
            if re.search('sklearn+',str(type(model))):
                v = self.predict_SKLearn(self._SKLearnVectoriser, model, features)
                votes.append(v)
            else:
                v = self.predict_NLTK(model, features[0])
                votes.append(v)
        return mode(votes)
        
    def confidence(self, features):
        votes = []
        for model in self._classifiers:
            if re.search('sklearn+',str(type(model))):
                v = self.predict_SKLearn(self._SKLearnVectoriser, model, features)
                votes.append(v)
            else:
                v = self.predict_NLTK(model, features[0])
                votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
    