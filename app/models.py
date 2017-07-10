from app import db

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twitter_id = db.Column(db.Integer, unique=T)
    user = db.Column(db.Integer, index=True)
    coordinates = db.Column(db.list)
    text = db.Column(db.string(140),index=True

    def __init__

    def __repr__(self):
        return '<Tweet: %r>' % (self.text)

class User(db.Model):

class Coordinates(db.Model):
