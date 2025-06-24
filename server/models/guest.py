from __init__ import db, SerializerMixin

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', back-populates = 'guest', cascade = 'all,delete-orphan')