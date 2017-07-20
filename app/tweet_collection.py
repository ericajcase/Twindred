from app import db
from .tweet import Tweet
from sqlalchemy.exc import IntegrityError

class TweetCollection(object):
    def __init__(self, search_term):
        self.hashtag = search_term

        self.tweetList  = list(Tweet.query.filter_by(search_term = self.hashtag).all())

        self.updateTweetList(self.searchTwitter())

    def searchTwitter():
        if len(self.tweetList) > 0:
            sinceId = Tweet.query.filter_by(search_term = self.hashtag)
        else:
            sinceId = None

        twit_search = TwitterApiWrapper()
        results = twit_search.all(hashtag, bigSearch = False, sinceID = sinceId)

        return (results)

    def __updateTweetList__(results):
        for result in results:
            unsaved = 0
            tweet = Tweet(result, search_term)
            db.session.add(tweet)
            try:
                db.session.commit()
                self.tweetList.append(tweet)
            except IntegrityError:
                db.session().rollback()
                unsaved += 1
