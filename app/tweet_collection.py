from app import db
from .tweet import Tweet
from sqlalchemy.exc import IntegrityError

class TweetCollection(object):
    def __init__(self, results,search_term):
        self.tweetList  = []
        self.make_tweetList(results, search_term)

    def make_tweetList(self, results,search_term):
        for result in results:
            tweetsAdded = 0
            tweet = Tweet(result, search_term)
            db.session.add(tweet)

            try:
                db.session.commit()
                self.tweetList.append(tweet)
            except IntegrityError:
                db.session().rollback()
