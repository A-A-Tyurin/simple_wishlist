''' Flask configuration. '''

from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    ''' Set flask configuration from .env file. '''

    # General configuration
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    # Database configuration
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
