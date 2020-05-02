from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import json
import matplotlib.pyplot as plt

# Use your Twitter Developer Account's Keys at below.
consumer_key = '************************'
consumer_secret = '*******************************************'
access_token = '**************************************************'
access_token_secret = '*********************************************'

count_p = 0
count_nu = 0
count_ne = 0

name = input("Enter twitter username:")

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

if __name__ == "__main__":
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name=name, count=200, tweet_mode='extended')

for tweet in tweets:
    b = tweet._json['full_text']
    analysis = TextBlob(b)
    x = analysis.sentiment.polarity
    if(x>0):
        count_p += 1
    elif(x==0):
        count_nu += 1
    elif(x<0):
        count_ne += 1
    else:
        pass

    
left = [1,2,3]
height = [count_p,count_nu,count_ne]
label = ['positive','neutral','negative']
plt.bar(left,height,tick_label=label,width = 0.5 ,color = ['green','blue','red'])
plt.xlabel('personality') 
plt.ylabel('no. of tweets') 
if (count_p>count_nu and count_p>count_ne):
    plt.title(name +  ' is positive')
elif(count_nu>count_p and count_nu>count_ne):
    plt.title(name+ ' is neutral')
elif(count_ne>count_p and count_ne>count_nu):
    plt.title(name+ ' is negative')
else:
    pass 
plt.show()  
