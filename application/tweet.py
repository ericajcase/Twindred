from app import db
import re
import tweepy
from tweepy import OAuthHandler
import jsonpickle
import os
from textblob import TextBlob

from sqlalchemy.dialects.postgresql import JSON
from geoalchemy2.types import Geography

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(500))
    twitter_id = db.Column(db.BigInteger, unique=True)
    text = db.Column(db.String(140),index=True)
    user = db.Column(db.BigInteger, index=True)
    date = db.Column(db.DateTime)
    coordinates = db.Column(Geography(geometry_type='POINT', srid=4326, spatial_index=True))
    location = db.column(db.String)
    polarity = db.Column(db.Float)
    subjectivity = db.Column(db.Float)

    def __init__(self, tweetData, search_term):
        self.twitter_id = tweetData.id
        self.user = tweetData.user.id
        self.text = tweetData.text
        self.date = tweetData.created_at
        self.search_term = search_term
        self.coordinates = None
        self.location = None

        self.polarity = 0
        self.subjectivity = 0
        self.get_tweet_sentiment()

        if tweetData.coordinates != None:
            self.update_coordinates(tweetData.coordinates['coordinates'])


    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)

    def update_coordinates(self,coords):
        self.location = "SRID=4326;POINT(%0.8f %0.8f)" % (coords[0], coords[1])

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        sentiment = TextBlob(self.clean_tweet(self.text)).sentiment

        self.polarity = sentiment.polarity
        self.subjectivity = sentiment.subjectivity
