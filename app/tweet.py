from app import db
import tweepy
from tweepy import OAuthHandler
import jsonpickle
import os



from sqlalchemy.dialects.postgresql import JSON
from geoalchemy2.types import Geography

class Tweet(db.Model):
    AUTH = os.environ['AUTH']
    API = tweepy.API(AUTH, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(139))
    twitter_id = db.Column(db.Integer, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    text = db.Column(db.String(140),index=True)
    user = db.Column(db.Integer, index=True)
    date = db.Column(db.DateTime)
    location = db.Column(Geography(geometry_type='POINT', srid=4326, spatial_index=True))

    def __init__(self, twitter_id, user, text, date, search_term, lon, lat):
        self.twitter_id = twitter_id
        self.user = user
        self.text = text
        self.date = date
        self.search_term = search_term
        self.location = Geography(geometry_type='POINT', srid=4326, spatial_index=True)

        self.update_location(lon,lat)

    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)

    def __update_location__(self,lon,lat):
        self.location = "SRID=4326;POINT(%0.8f %0.8f)" % (lon, lat)

    def get_tweets(self, searchTerm, bigSearch = False, sinceID = None, max_id = -1):
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
