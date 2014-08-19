__author__ = 'Orange'
from flask_wtf import Form
from wtforms import StringField,SelectMultipleField
from wtforms.validators import DataRequired, Length
from flask import session
from app.models import *

class AuthorForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])

class BookForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])
    authors = SelectMultipleField(u'Author list', choices=[(g.id, g.name) for g in Author.query.order_by('name').all()])

class SearchForm(Form):
    search = StringField('search', validators = [DataRequired()])