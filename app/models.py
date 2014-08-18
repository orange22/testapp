__author__ = 'Orange'
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import flask.ext.whooshalchemy as whooshalchemy
from database import Base
from app import app

class AuthorBook(Base):
    __tablename__ = 'author_book'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=False)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=False)
    author= relationship("Author")
    book = relationship("Book")

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    books = relationship("AuthorBook")


    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Book(Base):
    __tablename__ = 'book'
    __searchable__ = ['name']
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    authors = relationship("AuthorBook")

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Book %r>' % (self.name)

whooshalchemy.whoosh_index(app, Book)