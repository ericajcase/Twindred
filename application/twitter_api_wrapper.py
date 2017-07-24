import tweepy
from tweepy import OAuthHandler
import jsonpickle
import os

class TwitterApiWrapper(object):
    AUTH = tweepy.AppAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])

    API = tweepy.API(AUTH, wait_on_rate_limit=True,     wait_on_rate_limit_notify=True)

    def __initialize__(self):
        pass

    def all (self, searchTerm, bigSearch = False, sinceID = None, max_id = -1):
        if(not self.API):
            sys.exit(-1)

        tweets = []
        if bigSearch == True:
            maxTweets = 1000
        else:
             maxTweets = 10
        searchQuery = searchTerm  #search def
        tweetsPerQry = 100 # max permitted by Twitter
        tweetCount = 0
        fails = 0
        while ((len(tweets) < maxTweets) and fails < 10):
            try:
                print (self.API)
                new_tweets = self.API.search(q=searchQuery, count=tweetsPerQry,since_id = sinceID,  max_id=str(max_id - 1))
                if (len(new_tweets) > 0 ):
                    print("Downloaded {0} tweets".format(len(new_tweets)))
                    max_id = new_tweets[-1].id
                else:
                    fails += 1
                tweets += new_tweets
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
        return tweets
