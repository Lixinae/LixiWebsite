import os
import pathlib

# All base path to avoid copy past
basedir = os.path.abspath(os.path.dirname(__file__))
root_dir = pathlib.Path(__file__).parent.parent
web_static_dir = os.path.join(pathlib.Path(__file__).parent.parent, "web/static")
web_templates_dir = os.path.join(pathlib.Path(__file__).parent.parent, "web/templates")


class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')


class ProductionConfig(Configuration):
    DEBUG = False
    ASSETS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'convert_unicode': True,
                                 'connect_args': {'check_same_thread': False}}


class TestingConfig(Configuration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'convert_unicode': True,
                                 'connect_args': {'check_same_thread': False}}
