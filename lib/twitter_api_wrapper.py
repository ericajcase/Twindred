import tweepy
import jsonpickle
import os


class TwitterApiWrapper(object)

AUTH = os.env['AUTH']
API = tweepy.API(AUTH, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)


def __initialize__(self,searchTerm):


    def all (self, searchTerm, bigSearch = False, sinceID = None, max_id = -1):
        if(not self.API):
            sys.exit(-1)

        tweets = []
        if bigSearch:
            maxTweets = 10000
        else:
             maxTweets = 100
        searchQuery = searchTerm  #search def
        tweetsPerQry = 100 # max permitted by Twitter

        while len(tweets) < maxTweets:
            try:
                new_tweets = self.API.search(q=searchQuery, count=tweetsPerQry,since_id = sinceID,  max_id=str(max_id - 1))
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
        return tweets
