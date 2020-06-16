'''
Victor Sebastian Martinez
Youtube comment scraper

For preprocessing:
https://towardsdatascience.com/nlp-for-beginners-cleaning-preprocessing-text-data-ae8e306bef0f

Issues:
If there are non-english comments, the desired number of comments could not be met
the isEnglish functions sometimes classifies english sentences as non-english

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import sys
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from selenium import webdriver
from langdetect import detect

class Youtube():
    def __init__(self, terms, comments):
        self.driver = webdriver.Firefox(executable_path=r'.\geckodriver\geckodriver.exe')
        self.search_terms = str(terms[0])
        self.desired_comments = comments

    def isEnglish(self, sentence):
        try:
            return detect(sentence) == 'en'
        except:
            return False

    def remove_emoji(self,string):
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', string)

    def clean_comments(self, raw_comments):
        cleansed_comments = []
        for comment in raw_comments:
            if self.isEnglish(comment.text) and comment.text != '' or comment.text != ' ':
                clean_comment = self.remove_emoji(comment.text)
                cleansed_comments.append(clean_comment)
        return  cleansed_comments
    
    def search_video(self):
        # Search for a video
        self.driver.get("https://www.youtube.com/results?search_query=" + self.search_terms)
        Video = self.driver.find_element_by_xpath("//div[@class='text-wrapper style-scope ytd-video-renderer']")
        Video.click()
        time.sleep(3)

        comments = []
        # comment_section = self.driver.find_element_by_xpath('//*[@id="comments"]')
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        MAX_COMMENTS = self.driver.find_element_by_xpath("//*[@class='count-text style-scope ytd-comments-header-renderer']")
        MAX_COMMENTS = int(MAX_COMMENTS.text.split()[0].replace(",", ""))

        self.desired_comments = MAX_COMMENTS if self.desired_comments > MAX_COMMENTS else self.desired_comments

        # Scroll down until desired number of comments are reached
        while self.desired_comments > len(comments):
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)
            comments = self.driver.find_elements_by_xpath('//*[@id="content-text"]')

        # Preprocess and save
        stop_words = stopwords.words('english')
        tokenizer = RegexpTokenizer(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*") # \w - Any character, + - match one or more
        lemmatizer = WordNetLemmatizer()

        with open('Comments/youtube.txt', 'w') as f:
            comments = self.clean_comments(comments)
            for cmt in range(self.desired_comments):
                comment = comments[cmt]
                f.write(comment + '\n')
        self.driver.quit()












