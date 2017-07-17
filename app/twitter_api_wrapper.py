import tweepy
import jsonpickle
import os


class TwitterApiWrapper(object):

    # AUTH = os.environ['AUTH']
    # API = tweepy.API(AUTH, wait_on_rate_limit=True,
    # wait_on_rate_limit_notify=True)
    TWITTER_CONSUMER_KEY = 'uguoOjKuhh4rjy7bcefxhmwFWT'
    TWITTER_CONSUMER_SECRET =  'Y6FnSv75q5EX5x5Y7nk0Lsmimgc6b98aCMKdS7tryJJQK2rBBG'
    # TWITTER_ACCESS_TOKEN = '830437866027180032-seKWM1Wg1cMzStZYXXy9ecyVxWPjYmK'
    # TWITTER_ACCESS_SECRET = 'eprLYV9xGhVHp9KQrVyCRoNTJa95KzyAZVjXR1DrmLKRc


    # user_auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    # user_auth.set_access_token(TWITTER_ACCESS_TOKEN , TWITTER_ACCESS_SECRET)

    AUTH = tweepy.AppAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

    API = tweepy.API(AUTH, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


    def __initialize__(self):
        pass

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
            print(self.API)
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
