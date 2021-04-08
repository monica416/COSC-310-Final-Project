"""
Installation:
pip install tweepy 
"""

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import twitterCredentials

## Twitter Authenticater ##
def twitterAuthenticater():
    auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)

    return auth

## Get Tweets ##
def getTweets(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    tweets = []
    for tweet in Cursor(twitter_client.user_timeline, id = twitter_user).items(num_tweets):
        tweets.append(tweet.text)
    
    return tweets

## Get Retweets ##
def getRetweets(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    retweets = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        retweets.append(t.retweet_count)

    return retweets[0]

## Get likes ##
def getLikes(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    likes = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        likes.append(t.favorite_count)

    return likes[0]

## Get Date ##
def getDate(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)

    date = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        date.append(t.created_at)

    return date[0]

## Original Call From Other Classes ##
def getTweetInfo():
    user = input("IMDBOT: Enter their twitter handle to view their tweets: ")
    num = input("IMDBOT: How many tweets would you like to see? ")

    tweets_list = getTweets(user, int(num))

    for i in tweets_list:
        print("\n",i)

    ans = input("\nIMDBOT: Would you like a summary of their most recent tweet?")
    if (ans.lower()[0] == "y"):
        print("\n\n*** Most Recent Tweet ***")
        print(tweets_list[0])
        print("\n")
        
        rt = getRetweets(user, int(num))
        print("*** # of Retweets ***")
        print(rt, "\n")

        likes = getLikes(user, int(num))
        print("*** # of Likes ***")
        print(likes, "\n")

        date = getDate(user,int(num))
        print("*** Date and Time Created ***")
        print(date, "\n")

        length = len(tweets_list[0])
        print("*** Length of Tweet ***")
        print(length, "characters\n")
    else:
        pass

getTweetInfo()