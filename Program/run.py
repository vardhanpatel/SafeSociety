#!/usr/bin/env python
import time
from time import sleep
import random
import tweepy
#from our keys module (keys.py), import the keys dictionary

consumer_key = 'YOURKEY'
consumer_secret = 'YOURKEY'
access_token = 'YOURKEY'
access_token_secret = 'YOURKEY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.me()
print (user.name)

search_results = api.search(q="Someone Help Me", count=100)

sentences = 'Hi, I am a bot and i am repling to tweets with certain words and that is why i am talking to you, IF YOU REALLY NEED HELP PLEASE RESPOND BACK AND WE WILL TRY TO CHAT BACK TO YOU ASAP.',

for s in search_results:
        message = random.choice(sentences)
        sn = s.user.screen_name
        m = "@%s " % (sn) + str(sentences)
        s = api.update_status(m, s.id)
        sleep(2)
