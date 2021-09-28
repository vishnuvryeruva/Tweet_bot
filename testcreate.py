# By Nevil Shah and Vishnu

import unittest
import tweet_bot
import tweepy
import requests
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
mentions = api.user_timeline()
id=api.user_timeline()
# status = int(input('choose an id to delete'))
# delt = api.destroy_status(status)
resp = requests.get('http://127.0.0.1:5000/create')
posts = {}
author = []

class testcreate(unittest.TestCase): 
        
    def test_delete_tweet(self):
        self.assertEqual(str(resp),"<Response [200]>")

    def test_2(self):
        for mention in reversed(mentions):
            author.append(mention.user.name)
        x = len(mentions)
        self.assertEqual(author[x-1],"Khushil Modi")

    