from app import db
from sqlalchemy.dialects.postgresql import JSON

from geoalchemy2 import *

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
<<<<<<< Updated upstream
    twitter_id = db.Column(db.Integer, unique=True)
    user = db.Column(db.Integer, index=True)
    text = db.Column(db.string(140),index=True)

    def __init__(self):

    def __repr__(self):
        return '<Tweet: %r>' % (self.text)
=======
    search_term = db.Column(db.String(139))
    twitter_id = db.Column(db.Integer, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    text = db.Column(db.String(140),index=True)
    user = db.Column(db.Integer, index=True)
    date = db.Column(db.DateTime)
    location = db.Column(Geography(geometry_type='POINT', srid=4326, spatial_index=True))

    def __init__(self,args ):
        self.twitter_id = args[twitter_id]
        user = args[user]
        text = args[text]
        date = args[date]
        search_term = args[search_term]

    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)
>>>>>>> Stashed changes
