#!/usr/bin/env python
# encoding: utf-8
import os,sys
from twython import TwythonStreamer
import time
import argparser

argsfuc = argparser.ArgumentParser(description="Twitter Downloader")
argsfuc.add_argument('-kwf', dest='kwf', default='./keyword_list.txt', help='the keywords file')
argsv = argsfuc.parse_args()

APP_KEY=""
APP_SECRET=""
OAUTH_TOKEN=""
OAUTH_TOKEN_SECRET=""

class MyStreamer(TwythonStreamer):

    destfile='None'
    '''
    A sample of data jason:
    {u'quote_count': 0, 
    u'contributors': None, 
    u'truncated': True, 
    u'text': u'#cybersecurity #mustread BellaButler14RT SachinLulla: The DDoS Attack Against Dyn One Year Later\u2026 https://t.co/1KZNxndMZr', 
    u'is_quote_status': False, 
    u'in_reply_to_status_id': None, 
    u'reply_count': 0, 
    u'id': 928608104148697089, 
    u'favorite_count': 0, 
    u'entities': {u'user_mentions': [], u'symbols': [], u'hashtags': [{u'indices': [0, 14], u'text': u'cybersecurity'}, {u'indices': [15, 24], u'text': u'mustread'}], u'urls': [{u'url': u'https://t.co/1KZNxndMZr', u'indices': [98, 121], u'expanded_url': u'https://twitter.com/i/web/status/928608104148697089', u'display_url': u'twitter.com/i/web/status/9\u2026'}]}, 
    u'retweeted': False, 
    u'coordinates': None, 
    u'timestamp_ms': u'1510232399390', 
    u'source': u'<a href="http://www.powerapps.com" rel="nofollow">Microsoft PowerApps and Flow</a>', u'in_reply_to_screen_name': None, 
    u'id_str': u'928608104148697089', 
    u'retweet_count': 0, 
    u'in_reply_to_user_id': None, 
    u'favorited': False, 
    u'user': {u'follow_request_sent': None, u'profile_use_background_image': False, u'default_profile_image': False, u'id': 176498026, u'default_profile': False, u'verified': False, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/922552173082370049/aU47g53a_normal.jpg', u'profile_sidebar_fill_color': u'000000', u'profile_text_color': u'000000', u'followers_count': 713, u'profile_sidebar_border_color': u'000000', u'id_str': u'176498026', u'profile_background_color': u'000000', u'listed_count': 570, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme15/bg.png', u'utc_offset': 3600, u'statuses_count': 13246, u'description': u'share 2 evolve - ICT CIO #BIM Management #Audit #Hybrid #Cloud #Coaching #Digitalisierung #Engineering #CISO #DPO #GDPR #security #privacy #infosec #AI #MCSE', u'friends_count': 1386, u'location': u'always @ ro@d, @digitalization', u'profile_link_color': u'3B94D9', u'profile_image_url': u'http://pbs.twimg.com/profile_images/922552173082370049/aU47g53a_normal.jpg', u'following': None, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/176498026/1399796096', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme15/bg.png', u'name': u'Fridel Rickenb@cher', u'lang': u'de', u'profile_background_tile': False, u'favourites_count': 248, u'screen_name': u'fridel_on_road', u'notifications': None, u'url': u'http://www.mit-group.ch', u'created_at': u'Mon Aug 09 18:09:58 +0000 2010', u'contributors_enabled': False, u'time_zone': u'Bern', u'protected': False, u'translator_type': u'none', u'is_translator': False}, 
    u'geo': None, 
    u'in_reply_to_user_id_str': None, 
    u'possibly_sensitive': False, 
    u'lang': u'en', 
    u'extended_tweet': {u'display_text_range': [0, 177], u'entities': {u'user_mentions': [], u'symbols': [], u'hashtags': [{u'indices': [0, 14], u'text': u'cybersecurity'}, {u'indices': [15, 24], u'text': u'mustread'}, {u'indices': [121, 135], u'text': u'CyberSecurity'}, {u'indices': [136, 140], u'text': u'IoT'}, {u'indices': [141, 146], u'text': u'IIoT'}, {u'indices': [147, 160], u'text': u'DataSecurity'}, {u'indices': [161, 176], u'text': u'InternetOfThin'}], u'urls': [{u'url': u'https://t.co/hINhAFXvWn', u'indices': [97, 120], u'expanded_url': u'https://www.forbes.com/sites/davelewis/2017/10/23/the-ddos-attack-against-dyn-one-year-later/#1ba7a3a51ae9', u'display_url': u'forbes.com/sites/davelewi\u2026'}]}, u'full_text': u'#cybersecurity #mustread BellaButler14RT SachinLulla: The DDoS Attack Against Dyn One Year Later https://t.co/hINhAFXvWn #CyberSecurity #IoT #IIoT #DataSecurity #InternetOfThin\u2026'}, 
    u'created_at': u'Thu Nov 09 12:59:59 +0000 2017', 
    u'filter_level': u'low', 
    u'in_reply_to_status_id_str': None, 
    u'place': None}
    ###############***************************################
    The keywords in data dict:
    ['quote_count',
    'contributors',
    'truncated',
    'text',
    'is_quote_status',
    'in_reply_to_status_id',
    'reply_count',
    'id',
    'favorite_count',
    'source',
    'retweeted',
    'coordinates',
    'timestamp_ms',
    'entities',
    'in_reply_to_screen_name',
    'id_str',
    'retweet_count',
    'in_reply_to_user_id',
    'favorited',
    'user',
    'geo',
    'in_reply_to_user_id_str',
    'lang',
    'created_at',
    'filter_level',
    'in_reply_to_status_id_str',
    'place']
    '''
    def on_success(self, data):                                
        if ('text' in data) and (data['is_quote_status'] == False) and (data['retweeted'] == False) and (data['lang'] == 'en'):
            info = data['id_str'] + '<|||||>' + data['text'] + '<|||||>' + data['source'] + '<|||||>' + data['created_at']
            open(destfile, 'a').write(info.encode('utf-8'))                                      
            print(info)                                           
            print '###########'
 
    def on_error(self, status_code, data):
        if status_code == 402:
            time.sleep(600)
        print(status_code)

def cracker(keyword_list):
    lista = keyword_list
    for idx,itm in enumerate(lista):
        locals()['twlisten'+str(idx)] = MyStreamer(consumer_key, consumer_secret, access_key, access_secret)
        locals()['twlisten'+str(idx)].destfile = ('./data/'+itm+'.txt').replace(' ', '_')
        locals()['twlisten'+str(idx)].statuses.filter(track=itm)
    return True

if __name__ == '__main__':
    
    tkeys = [itm.strip() for itm in open(argsv.kwf, 'r').readlines()]
    cracker(tkeys)


