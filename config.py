__author__ = 'orange'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY='123'
WHOOSH_BASE = os.path.join(basedir, 'search.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')