from application import db
from .tweet import Tweet
from sqlalchemy.exc import IntegrityError
from .twitter_api_wrapper import TwitterApiWrapper

class TweetCollection(object):
    def __init__(self, search_term):
        self.hashtag = search_term

        self.tweetList  = list(Tweet.query.filter_by(search_term = self.hashtag).all())

        self.updateTweetList(self.searchTwitter())

    def searchTwitter(self):
        if len(self.tweetList) > 0:
            sinceId = Tweet.query.filter_by(search_term = self.hashtag)
        else:
            sinceId = None

        twit_search = TwitterApiWrapper()
        results = twit_search.all(self.hashtag, bigSearch = False, sinceID = sinceId)

        return (results)

    def updateTweetList(self,results):
        for result in results:
            unsaved = 0
            tweet = Tweet(result, self.hashtag)
            db.session.add(tweet)
            try:
                db.session.commit()
                self.tweetList.append(tweet)
            except IntegrityError:
                db.session().rollback()
                unsaved += 1


    def by_sentiment(self, polarity):

        pos = [tweet for tweet in self.tweetList if tweet.polarity > polarity]

        neg = [ tweet for tweet in self.tweetList if tweet.polarity < -(polarity) and tweet.subjectivity > 0.5]

        return {
            "num_pos": len(pos),

            "num_neg": len(neg),

            "most_pos": list(Tweet.query.filter_by(search_term = self.hashtag).filter(Tweet.subjectivity > 0.5).order_by(Tweet.polarity.desc()).limit(10).all()),

            "most_neg": list(Tweet.query.filter_by(search_term = self.hashtag).filter(Tweet.subjectivity > 0.5).order_by(Tweet.polarity).limit(10).all())
            }
