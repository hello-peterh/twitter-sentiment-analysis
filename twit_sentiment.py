#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:04:02 2018

@author: peterhung
"""

import json
import matplotlib.pyplot as plt
from textblob import TextBlob

with open('tweet_stream_China_10000.json') as infile:
    data1 = json.load(infile)

with open('tweet_stream_usa_10000.json') as infile:
    data2 = json.load(infile)

#SENSANAL
sens_lst = []
for item in data1:
    tweets = item['text']
    sens_lst.append(tweets)

for item in data2:
    tweets = item['text']
    sens_lst.append(tweets)

sub_lst = []
pol_lst = []

for s in sens_lst:
    tb = TextBlob(s)
    sub_lst.append(tb.sentiment.subjectivity)
    pol_lst.append(tb.sentiment.polarity)
    
#Finding the average
sub_avg = sum(sub_lst)/len(sub_lst)
pol_avg = sum(pol_lst)/len(pol_lst)
print(sub_avg,pol_avg)
    
plt.hist(sub_lst, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('subjectivity score')
plt.ylabel('tweet count')
plt.grid(True)
plt.savefig('subjectivity_tweets.pdf')
plt.show()

plt.hist(pol_lst, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('polarity score')
plt.ylabel('tweet count')
plt.grid(True)
plt.savefig('polarity_tweets.pdf')
plt.show()