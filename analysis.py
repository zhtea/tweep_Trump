# -*- coding: utf-8 -*- 
import re
import pickle
from textblob import TextBlob

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
good_comment = set()
with open("good_comment.txt",'r',encoding='gb18030') as f:
    while True:
        line = f.readline().strip()
        if line == '':
            break
        good_comment.add(line)
    print("length of good comment is "+str(len(good_comment)))
bad_comment = set()
with open("bad_comment.txt",'r',encoding='gb18030') as f:
    while True:
        line = f.readline().strip()
        if line == '':
            break
        bad_comment.add(line)
    print("length of bad comment is "+str(len(bad_comment)))
good = 0
bad = 0
count = 0
dic_good = {}
dic_bad = {}
with open("Trump.txt",'r',encoding='utf-8') as f:
    while True:
        tweet = f.readline().strip()
        if tweet == '':
            break
        tweet = preprocess(tweet)
        tweet_analysis = TextBlob(' '.join(tweet))
        if tweet_analysis.sentiment.polarity>0:
            good+=1
        if tweet_analysis.sentiment.polarity<0:
            bad+=1
        """
        for word in tweet:
            if word in good_comment:
                good +=1
                dic_good[word] = dic_good.get(word,0)+1
                break
            if word in bad_comment:
                bad +=1
                dic_bad[word] = dic_bad.get(word,0)+1
                break
        """
        count +=1
print("good comment is "+str(good)+"; bad comment is "+str(bad)+"; and total is "+str(count))
with open("dic_good.txt",'wb') as f:
    pickle.dump(dic_good,f)
with open("dic_bad.txt","wb") as f:
    pickle.dump(dic_bad,f)

