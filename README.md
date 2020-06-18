# SentimentAnalysis

Natural language processing python system in charge of categorize comments made in different media as positive or negative. The method used consisted of a voting system between the distinct models to calculate the sentiment analysis.
The methods used to classify are:
- Naive Bayes
- Bernoulli Naive Bayes
- Multinomial Naive Bayes
- LogisticRegression

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
From this social media collects all the new tweets about the term you choose. It can accept a list of terms. If the terms are trending topics it recollect faster the tweets, if it is not a trending topic it may takes a little more minutes to respond.

### Example: 
main.py -m twitter -c 50

insert terms: 
covid19 coronavirus covid

Comments/twitter.py
```
More likely infected via chemtrails.
: In a one-of-a-kind election amid , elects , , , &amp; as non-
: Vice President Pence claimed success because COVID-19 deaths are down to fewer than a day.That's more than a m
: % of COVID-19 nursing home deaths came from just five states.New York, New Jersey, Michigan, California, and Pennsylv
: % of Black immigrant domestic workers who provide critical care for families have lost their jobs or had hours reduced dur
Thousands of families like Sara + Omar have faced separation for years because of the 's cruel spouse
``` 

### Results 
![Alt text](example/results/covid.png?raw=true "Title")

