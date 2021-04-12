"""
Installation:
pip install tweepy 
"""
import tweepy as tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import twitterCredentials


## Twitter Authenticater ##
"""
Gets the Keys and Tokens from twitterCredentials.py and make sure the accound is authenticated in order to 
gain access to twitter

Returns this authentication for later use
"""
def twitterAuthenticater():
    auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)

    return auth

## gets access to API using authenticater ##
api = tweepy.API(twitterAuthenticater())

## Get Tweets ##
"""
Gets the latest / most recent tweets from the specified user
"""
def getTweets(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    tweets = []
    for tweet in Cursor(twitter_client.user_timeline, id = twitter_user).items(num_tweets):
        tweets.append(tweet.text)
    
    return tweets

## Get Retweets ##
"""
Gets the retweet infromation for the specified user's most recent tweet
"""
def getRetweets(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    retweets = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        retweets.append(t.retweet_count)

    return retweets[0]

## Get likes ##
"""
Gets the like infromation for the specified user's most recent tweet
"""
def getLikes(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)
    
    likes = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        likes.append(t.favorite_count)

    return likes[0]

## Get Date ##
"""
Gets the date and time infromation for the specified user's most recent tweet
"""
def getDate(twitter_user, num_tweets):
    auth = twitterAuthenticater()
    twitter_client = API(auth)

    date = []

    for t in Cursor(twitter_client.user_timeline, id = twitter_user).items(1):
        date.append(t.created_at)

    return date[0]

## Get Tweet Info ##
"""
Gets the tweet information depending on what the user specifies

This includes the most recent tweets and a summary of the most recent tweet
"""
def getTweetInfo(user):
    if (user == " "):
        pass
    else:
        num = input("IMDBot: How many tweets would you like to see? ")

        tweets_list = getTweets(user, int(num))

        print("IMDBot: Showing " + user + "'s " + num + " most recent tweet(s): ")
        for i in tweets_list:
            print("\n",i)

        ans = input("\nIMDBot: Would you like a summary of their most recent tweet?      ")
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


## Search for User ##
"""
This class searches for the username / twitter handle based on the name / person that was being talked about
"""
def searchUser(name):
    results = []
    userName = " "
    found = False
    idx = 0

    for i , user in enumerate(tweepy.Cursor(api.search_users, q = name).items(5)):
        results.append(user.screen_name)

    while (found == False and idx <= len(results)):
        print("IMDBot: ", results[idx])
        ans = input("IMDBot: Is this the correct twitter handle?      ")

        if (ans.lower()[0] == 'y'):
            found = True
            userName = results[idx]
        else:
            idx += 1
    
    if (found == False):
        print("IMDBot: Sorry, there is no twitter account for that person")
    else:
        getTweetInfo(userName)

## Wants twitter info ##
"""
First class that is called

Asks the user if they would like to view tweets
"""
def wantsTwitterInfo(user):
    view = input("IMDBot: Would you like to view " + user + "'s tweets? ")

    if (view.lower()[0] == "y"):
        searchUser(user)
    else:
        pass


## --- For Testing --- ##
#searchUser("Ryan Reynolds")