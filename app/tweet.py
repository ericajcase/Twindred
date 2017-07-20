from app import db
import tweepy
from tweepy import OAuthHandler
import jsonpickle
import os

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
    location = db.Column(Geography(geometry_type='POINT', srid=4326, spatial_index=True))

    def __init__(self, tweetData, search_term):
        self.twitter_id = tweetData.id
        self.user = tweetData.user.id
        self.text = tweetData.text
        self.date = tweetData.created_at
        self.search_term = search_term
        self.location = tweetData.coordinates
        # self.location = coordinates Geography(geometry_type='POINT', srid=4326, spatial_index=True)

        # self.update_location(lon,lat)
    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)

    def __update_location__(self,lon,lat):
        self.location = "SRID=4326;POINT(%0.8f %0.8f)" % (lon, lat)
