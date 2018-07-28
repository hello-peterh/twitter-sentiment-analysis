#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:47:18 2018

@author: peterhung
"""

import json
from  collections import Counter
from pprint import pprint
import nltk
import string
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

with open('tweet_stream_fortnite_10000.json') as infile:
    data = json.load(infile)


ls = LancasterStemmer()
ps = PorterStemmer()
ss = SnowballStemmer("english")
wnl = WordNetLemmatizer()
    
    
#pprint(data[0])
'''
mention_list = []
for item in data:
    mentions = item['entities']['user_mentions']
    for ment in mentions:
        mention_list.append(ment['screen_name'])
        
c = Counter(mention_list)
print(c.most_common())
'''
#COLLECTING TOP 10 WORDS IN TWEETS
tweets_lst = []
punc = string.punctuation

for item in data:
    tweets = item['text']
    for i in tweets.split():
        if '@' not in i and 'http' not in i:
            table = str.maketrans({key: None for key in string.punctuation}) #https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
            text_nopunc = i.translate(table)
            text_stem = ss.stem(text_nopunc)
            #print(text_nopunc)
            tweets_lst.append(text_nopunc.lower())
            
stopwords = nltk.corpus.stopwords.words('english')

#Include unique twitter words in stopwords
#new_words = ['fortnite', 'one', 'follow', 'win', 'vbuck', 'retweet', 'enter', 'give', 'pick', 'play']
#for n in new_words:
    #stopwords.append(n)

tweets_final = []

for i in tweets_lst:
    if i not in stopwords and len(i)>2:
        tweets_final.append(i)

c = Counter(tweets_final)
print('The top 10 words')
for i in c.most_common(10):
    print(i[0]+'='+str(i[1]))

#COLLECTING TOP 10 HASHTAGS
hashtags_list = []
for item in data:
    hashtags = item['entities']['hashtags']
    for ht in hashtags:
        hashtags_list.append(ht['text'])
        
c2 = Counter(hashtags_list)
print('The top 10 hashtags')
for i in c2.most_common(10):
    print(i[0]+'='+str(i[1]))

#COLLECTING TOP 10 USERMENTIONS

mention_list = []
for item in data:
    mentions = item['entities']['user_mentions']
    for ment in mentions:
        mention_list.append(ment['screen_name'])

c3 = Counter(mention_list)
print('The top 10 user mentions')
for i in c3.most_common(10):
    print(i[0]+'='+str(i[1]))

#COLLECTING TOP 10 USER NAMES
users_list = []
for item in data:
    users = item['user']['screen_name']
    users_list.append(users)
        
c4 = Counter(users_list)
print('The top 10 user names')
for i in c4.most_common(10):
    print(i[0]+'='+str(i[1]))

#MOST INFLUENTIAL TWEET

infl_score = 0
top_tweet = ''
for item in data: #Is it, the tweet that was collected, which one was retweeted the most OR, our of all the tweets,the ones that were retweets, which one was retweeted the most
    try:
        rt_c = item['retweeted_status']['retweet_count']
        rep_c = item['retweeted_status']['reply_count']
        quo_c = item['retweeted_status']['quote_count']
        tot = rt_c + rep_c + quo_c
        if tot > infl_score:
            infl_score = tot
            tweet = item['text']
            top_tweet = tweet
    except:
        continue

print(top_tweet)

    



