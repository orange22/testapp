__author__ = 'orange'
#from app import db
from app import app
import flask.ext.whooshalchemy as whooshalchemy

ROLE_USER = 0
ROLE_ADMIN = 1

class Book(db.Model):
    __searchable__ = ['name']
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Book %r>' % (self.name)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % (self.name)

whooshalchemy.whoosh_index(app, Book)