from models.__init__ import db, SerializerMixin
from flask import Flask


class Guest(db.Model, SerializerMixin):
    __tablename__ ='guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    serialize_only = ('id','name', 'occupation', )
    
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Guest {self.id} {self.name} in {self.occupation}>'
    
      
    