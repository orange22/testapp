__author__ = 'Orange'
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask import session

class AuthorForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])

class BookForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])

class SearchForm(Form):
    search = StringField('search', validators = [DataRequired()])