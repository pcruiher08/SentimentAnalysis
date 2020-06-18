# SentimentAnalysis

Natural language processing python system in charge of categorize comments made in different media as positive or negative. The method used consisted of a voting system between the distinct models to calculate the sentiment analysis.
The methods used to classify are:
- Naive Bayes (NLTK)
- Bernoulli Naive Bayes (SKLearn)
- Multinomial Naive Bayes (SKLearn)
- LogisticRegression (SKLearn)
- Vader

## Requirements
Before running the main you must execute the following pip command\
pip install -r requirements.txt

This will install all the required dependencies for the compiler to run:
- nltk
- langdetect
- pandas
- selenium
- matplotlib
- vadersentiment
- config
- tweepy
- preprocessor
- SpeechRecognition
- pyaudio

You must need to get your twitter API keys in order to run the system. You can get them here:\
https://developer.twitter.com/. Also add a file call config.py and set your keys like this: 

```
keys = {
    "ckey"   : "xxxxxxxxxxxxxxxxxxxxxx",
    "csecret": "xxxxxxxxxxxxxxxxxxxxxx",
    "atoken" : "xxxxxxxxxxxxxxxxxxxxxx",
    "asecret": "xxxxxxxxxxxxxxxxxxxxxx"
}
```
If you are a windows user after running the requirements you must need to run this for the recognition voice option:
```
pipwin install pyaudio
```

## Usage
main.py -m < twitter|youtube|voice > \
main.py -m < twitter|youtube|voice > -c 100

| Command |  Default | Description |
| --- | --- | --- |
| `-m` | -- | Set the mode you want to choose. Available options: *twitter, youtube, voice* |
| `-c` | 100 | Set the counter for how many tweets or comments ( youtube ) to search |


## Twitter API - StreamListener
From this social media collects all the new tweets about the term you choose. It can accept a list of terms. If the terms are trending topics it recollects the tweets faster, if it is not a trending topic it may takes a little more minutes to respond.

### Example: 
main.py -m twitter -c 50

insert terms: 
covid19 coronavirus covid

Comments/twitter.py
```
: We all got that covid
You cant get covid19 at Dem / Commie congregations. Hating America is the vaccine against all pande
: Baffled by the links between smoking, nicotine and COVID-19? Me too, but take a look at my effort to make sense of it for
: The federal government is stuck with million doses of hydroxychloroquine now that the FDA has revoked permission for the anti-m
: If there is a massive covid outbreak at a Trump rally, is that a Klandemic?
: "are you wearing the C"the CDC recommended face covering because were still in the middle of the global COVID-19 pand
``` 

### Results 
![Alt text](example/results/covid.png?raw=true "Title")

