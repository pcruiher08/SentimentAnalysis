# SentimentAnalysis

A natural language processing system in charge of categorizing comments made in different social media as positive or negative. The method used consisted of a voting system of different models to make sentiment analysis predictions.
The methods used to classify are:
- Naive Bayes (NLTK)
- Bernoulli Naive Bayes (SKLearn)
- Multinomial Naive Bayes (SKLearn)
- LogisticRegression (SKLearn)
- Vader

## Requirements
Before running the main you must execute the following pip command\

```
pip install -r requirements.txt
```

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
If you are a windows user after running the requirements you must need to run this for the voice recognition option:
```
pip install pipwin
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
![Alt text](example/results/twitter.png?raw=true "Title")

## Yotube Web Scrapper
From this social media collects all the comments about the term you choose. It select the most recent video related to the term and collects its comments.


### Example: 
main.py -m youtube -c 5

insert terms: 
covid19

Comments/youtube.txt

```
They are literally publishing the same story every 6 hours.
If you get it, more than likely you'll be fine.
Nothing 10 thousand protesters standing next to each other can�t fix.
I think its weird that out of no where when the riots were going on no one talked about covid. And now all of a sudden once riots start going away then covid comes back. Kinda odd
Montana is up by a 110% because there were like 7 cases daily before
```
### Results 
![Alt text](example/results/youtube.png?raw=true "youtube")

## Voice - PyAudio
This dependency transcript the audio input of the user. It doesn't need a counter parameter as it just analyze it as 1 entry. 

### Example: 
main.py -m voice

insert terms: \
*hi I am really happy today*

### Results 
![Alt text](example/results/voice.png?raw=true "pyAudio")
