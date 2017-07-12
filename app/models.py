from app import db
from sqlalchemy.dialects.postgresql import JSON

from geoalchemy2.types import Geography

class Tweet(db.Model):
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

    def update_location(self,lon,lat):
        self.location = "SRID=4326;POINT(%0.8f %0.8f)" % (lon, lat)

    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)
