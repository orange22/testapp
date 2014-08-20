__author__ = 'Orange'
#from sqlalchemy import Table, Column, Integer, String, ForeignKey
#from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.declarative import declarative_base
from database import Base


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    authors = association_proxy('author_book', 'author')

    def __init__(self, name=None, authors=None):
        self.name = name
        self.authors = authors

    def __repr__(self):
        return '<Book %r>' % (self.name)

class AuthorBook(Base):
    __tablename__ = 'author_book'
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)

    book = relationship(Book,
                backref=backref("author_book",
                                cascade="all, delete-orphan")
            )

    author = relationship("Author")

    def __init__(self, author=None, book=None, special_key=None):
        self.author = author
        self.book = book

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    books = relationship("AuthorBook")


    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % (self.name)
