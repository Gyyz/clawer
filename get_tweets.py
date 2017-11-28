from tweepy import OAuthHandler
import tweepy

import codecs
import time
import os

consumer_key = "="
consumer_secret = "="

access_token = "="
access_token_secret = "="

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(query)
    results = []
    tweets = tweepy.Cursor(api.search, q='%s' % query, lang='en').items(5000):
    for itm in tweets:
        results.append(itm.text)

    filtweets=[]
    for t in set(results):
        words=t.split()
        if len(words)>5:
            filtweets.append(t)
    with codecs.open('%s_keyword.txt', 'w', 'utf-8') as wrout:
        wrout.write('\n'.join(filtweets))


def writeToFile(path,tweets):
    output = codecs.open(path, 'w', 'utf-8')
    output.write('\n'.join([r for r in set(tweets)]))

#results=getTweets('NASA')
#
#writeToFile('1.txt',results)


