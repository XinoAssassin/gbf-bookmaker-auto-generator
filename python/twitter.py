import sys
import os
import tweepy
import json

# Consumer keys and access tokens, used for OAuth

 
# Sample method, used to update a status
# api.update_status('Hello Form RBI Lab!')

# load image

def sendImage(tweet, imagePath):
    config = json.load(open("twitter.json"))
    print(config)
    consumer_key = config["consumerKey"]
    consumer_secret = config["consumerSecret"]
    access_token = config["accessToken"]
    access_token_secret = config["accessTokenSecret"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.me()
    print('Name: ' + user.name)
    print('Friends: ' + str(user.friends_count))
    api.update_with_media(imagePath, tweet)
