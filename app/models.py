__author__ = 'Orange'
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from database import Base
from app import app

#class AuthorBook(Base):
#    __tablename__ = 'author_book'
#    id = Column(Integer, primary_key=True)
#    author_id = Column(Integer, ForeignKey('author.id'), primary_key=False)
#    book_id = Column(Integer, ForeignKey('book.id'), primary_key=False)
#    author= relationship("Author")
#    book = relationship("Book")

#    def __init__(self, name=None):
#        self.author_id = author_id
#        self.name = name
#
#    def __repr__(self):
#        return '<Book %r>' % (self.name)

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    #books = relationship("AuthorBook")


    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    #authors = relationship("AuthorBook")
    authors = relationship("Author", secondary=lambda: author_book)

    def __init__(self, name=None, authors=None):
        self.name = name
        self.authors = authors

    def __repr__(self):
        return '<Book %r>' % (self.name)

author_book = Table('author_book', Base.metadata,
    Column('author_id', Integer, ForeignKey("author.id"),
           primary_key=True),
    Column('book_id', Integer, ForeignKey("book.id"),
           primary_key=True)
)