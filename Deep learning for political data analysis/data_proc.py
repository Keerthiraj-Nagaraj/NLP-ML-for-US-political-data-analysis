# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:50:19 2019

@author: keert
"""

import pickle as pk

import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tag import pos_tag


from wordcloud import WordCloud, STOPWORDS



[lib, con, neutral] = pk.load(open('ibcData.pkl', 'rb'))

conser = ""

for tree in con:
    conser += tree.get_words()


liber = ""

for tree in lib:
    liber += tree.get_words()
    
neut = ""

for tree in neutral:
    neut += tree.get_words()
    
    
    
text = neut
# Create tokenizer
tokenizer = RegexpTokenizer('\w+')
# Create tokens
tokens = tokenizer.tokenize(text)
# Initialize new list
words = []
# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())
# Get English stopwords and print some of them

sw = nltk.corpus.stopwords.words('english')
# Initialize new list
words_ns = []
# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

tagged_words = pos_tag(words_ns)

nouns = [word for word,pos in tagged_words if pos == 'NN']

uniqueWords = [] 
for i in nouns:
      if not i in uniqueWords:
          uniqueWords.append(i);
    
atext = " "
for n in nouns:
    if len(n) > 3:
        atext += n
        atext += " "
    
        
sns.set()
freqdist1 = nltk.FreqDist(nouns)
freqdist1.plot(10)

wordcl = WordCloud(background_color= "white", stopwords=STOPWORDS, max_words= 20).generate(atext)

plt.imshow(wordcl, interpolation='bilinear')
plt.axis("off")
plt.show()    
