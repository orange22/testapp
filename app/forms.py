__author__ = 'Orange'
from flask_wtf import Form
from wtforms import StringField,SelectMultipleField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length
from flask import session
from app.models import *

class AuthorForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])

class BookForm(Form):
    id = StringField('id')
    name = StringField('name', validators=[DataRequired()])
    authors = SelectMultipleField(u'Author list', choices = [(g.id, g.name) for g in Author.query.all()])

class SearchForm(Form):
    search = StringField('search', validators = [DataRequired()])

def check_login(form, field):
    if field.data != 'admin':
        raise ValidationError('Field must be less than 50 characters')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(),check_login])
    password = PasswordField('Password', validators=[DataRequired(),check_login])