#!/usr/bin/env python
# encoding: utf-8
#download all the tweets of one usr
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json

argsfuc = argparser.ArgumentParser(description="Twitter Downloader")
argsfuc.add_argument('-kwf', dest='kwf', default='./keyword_list.txt', help='the keywords file')
argsv = argsfuc.parse_args()


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir, query):

        query_fname = query.replace(' ', '_')
        self.outfile = "%s/stream_%s.txt" % (data_dir, query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def cracker(keywordls):
    lista = keywordls
    for idx,itm in enumerate(lista):
        locals()['listen'+str(idx)] = Stream(auth, MyListener(args.data_dir, itm))
        locals()['listen'+str(idx)].filter(track=[itm])
    return True

if __name__ == '__main__':
    tkeys = [itm.strip() for itm in open(argsv.kwf, 'r').readlines()]
    cracker(tkeys)