import sys, os, time
import tweepy
# to try import simplejson
try:
    import simplejson as json
except ImportError:
    import json

# read file
with open('config.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

keys = dict(
consumer_key = obj['consumer_key'],
consumer_secret = obj['consumer_secret'],
access_token = obj['access_token'], 
access_token_secret = obj['access_token_secret']
)

user = obj['user']

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet() 