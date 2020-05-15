import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Configuration):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Configuration):
    TESTING = True
