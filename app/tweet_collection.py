class TweetCollection(object)
    def __initialize__(self, twitterResponse):
        tweetList  = make_tweetList(twitterResponse)

    def __make_tweetList__(self, results):
        tweetList = []
        for result in results:
            tweetList += Tweet(result)
