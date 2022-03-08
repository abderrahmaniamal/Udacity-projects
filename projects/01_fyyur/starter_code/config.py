import os

import sqlalchemy

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False


# Connect to the database


# TODO IMPLEMENT DATABASE URL


DATABASE_URL =  'postgresql://postgres:Lamlouma@localhost:5432/DB'
#SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
SQLALCHEMY_DATABASE_URI = DATABASE_URL

