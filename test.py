import tweepy
import json

from tweepy import OAuthHandler

consumer_key = 'yMRKHnT3x8Vyhp4rRY0zofBJA'
consumer_secret = 'mNDHRyoSko64x9mIr241rOZcJvVRADKFkNmUZajv8lHRsD5VQS'
access_token = '2378992174-YfR2egNwWGACPM93x1yOFdcm69XcLc6Qs6ecwlo'
access_secret = 'GnOyHVgsifMMgfkTF1OQ7xUQ1D7JvHEP8h0xbXiFwt93c'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)


