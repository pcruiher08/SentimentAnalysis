from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from decimal import Decimal

def analyze(comment):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(comment)
    confidence = Decimal(result['compound']+1)/2  #proporcion
    classification =  'neg' if confidence < 0.5 else 'pos' 
    #print(classification,confidence)
    return classification,confidence