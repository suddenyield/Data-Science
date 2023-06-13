# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:06:14 2023

@author: gianl
"""

from textblob import TextBlob
file_path = 'mytext.txt'
with open(file_path, 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)

