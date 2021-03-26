import os
import pathlib

# All base path to avoid copy past
# Also if we move the file from the "application" folder, we need to change the values here
basedir = os.path.abspath(os.path.dirname(__file__))
root_dir = pathlib.Path(__file__).parent.parent
web_static_dir = os.path.join(pathlib.Path(__file__).parent.parent, "web/static")
web_dynamic_dir = os.path.join(pathlib.Path(__file__).parent.parent, "web/dynamic")
web_templates_dir = os.path.join(pathlib.Path(__file__).parent.parent, "web/templates")


class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')


class ProductionConfig(Configuration):
    DEBUG = False
    ASSETS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'mysql+pymysql://root:admin@192.168.1.37:3306/vahenWeb_prod'
    # 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'convert_unicode': True,
                                 'pool_recycle': 500, }


class DevelopmentConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'mysql+pymysql://root:admin@192.168.1.37:3306/vahenWeb_dev'
    # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'convert_unicode': True,
                                 'pool_recycle': 500, }
    # 'connect_args': {'check_same_thread': False}}


class TestingConfig(Configuration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'mysql+pymysql://root:admin@192.168.1.37:3306/vahenWeb_test'
    # 'sqlite:///' + os.path.join(basedir, 'test.db')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'convert_unicode': True,
                                 'pool_recycle': 500, }
    # 'connect_args': {'check_same_thread': False}}
