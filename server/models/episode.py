from __init__ import db, SerializerMixin

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.String)