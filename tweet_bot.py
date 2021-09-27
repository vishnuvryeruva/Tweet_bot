import tweepy
import time
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def create():
    tweet = input("Enter tweet to post:")
    newt = api.update_status(tweet)
    print('%s is tweeted',newt)

def retrieve_tweet():
    mentions = api.user_timeline()
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text, flush=True)

def delete_tweet():
    id = api.user_timeline()
    for i in reversed(id):
        print(str(i.id) + ' - ' + i.text, flush=True)
    status = int(input('choose an id to delete'))
    delt = api.destroy_status(status)
    print('%s is deleted',delt)

# def reply():
#     mentions = api.user_timeline()
#     for mention in reversed(mentions):
#         print(str(mention.id) + ' - ' + mention.text, flush=True)
#         id = int(input('enter ID to reply: '))
#         # tweet = input('enter msg to reply: ')
#         api.update_status('@' + mention.user.screen_name + 'Hi test reply', id)
# while True:
#     reply()
#     time.sleep(15)