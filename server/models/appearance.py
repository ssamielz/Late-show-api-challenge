from __init__ import db, SerializerMixin

class Appearance(db.Model):
    __tablename__= "appearances"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String)
    guest_id = db.Column(db.String, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.String, db.ForeignKey('episodes.id'))

    guest = db.relationship('Guest', back-populates='appearances')
    episode = db.relationship('Episode', back-populates='appearances')
    