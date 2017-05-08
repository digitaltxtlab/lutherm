#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
import and preprocess M. Luther's collected writings
"""
__author__      = "K.L. Nielbo"

import io, os, glob, re
from nltk.corpus import stopwords

def readalpha(filename):
    """import unicode plain, remove punctuation and numerals and casefold """
    f = io.open(filename, 'r' ,encoding = 'utf-8')
    content = f.read()
    content = re.sub(r'\W+', ' ',content)
    content = re.sub(r'\d','',content)
    content = content.lower()
    return content

def cleanstop(var, language = 'english'):
    """ stopword removal from var (string or list of tokenized words) based on language from Porter et al"""
    stopword_l = set(stopwords.words(language))
    if (type(var) == str) or (type(var) == unicode):
        res = ' '.join([w for w in var.lower().split() if w not in stopword_l]) 
    else:
        res = [w for w in var if w.lower() not in stopword_l]
    return res

def cleanlat(s):
    """ revome latin stopwords based on local list """
    stoplat = io.open(os.path.expanduser('~/Documents/lang_res/latin.txt'),encoding='utf-8').read().split()
    res = ' '.join([w for w in s.lower().split() if w not in stoplat])
    return res    

## main
datadir = '~/Documents/proj/lutherm/data/'
datadir = os.path.expanduser(datadir)
files = glob.glob(datadir+'*.txt')
doc_list = []
for f in files:
    doc = readalpha(f)
    doc = cleanstop(doc,'german')
    doc = cleanlat(doc)
    doc_list.append(doc)

# word cloud for inspection
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud().generate(' '.join(doc_list))
plt.figure(figsize=(18,18),dpi=300)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png',bbox_inches='tight')
# plt.show()





