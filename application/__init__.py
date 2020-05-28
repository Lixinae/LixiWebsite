import logging

from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_assets import Environment
from application.configuration import DevelopmentConfig, ProductionConfig
from application.assets import create_static_bundles_assets

# db = SQLAlchemy()
# migrate = Migrate()
from application.logger import setup_logging

bootstrap = Bootstrap()


# Enregistrement des blueprint
def blueprint_registrations(current_app):
    """
    Register the blueprints for the app
    :param current_app: The app we are using
    """
    # from application.cv import cv_bp
    from application.index import index_bp
    # from application.contact import contact_bp
    from application.errors import errors_bp
    from application.portfolio import portfolio_bp
    from application.passions import passions_bp
    from application.apps import apps_bp
    from application.apps.webcrawler import webcrawler_bp
    # from application.apps.acronymos import acronymos_bp
    from application.apps.anagramos import anagramos_bp
    from application.apps.stringToLeet import string_to_leet_bp

    # current_app.register_blueprint(cv_bp)
    # current_app.register_blueprint(contact_bp)

    # Index
    current_app.register_blueprint(index_bp)

    # Errors
    current_app.register_blueprint(errors_bp)

    # Portfolio
    current_app.register_blueprint(portfolio_bp)

    # Passions
    current_app.register_blueprint(passions_bp)

    # Apps
    current_app.register_blueprint(apps_bp)
    current_app.register_blueprint(webcrawler_bp)
    # current_app.register_blueprint(acronymos_bp)
    current_app.register_blueprint(anagramos_bp)
    current_app.register_blueprint(string_to_leet_bp)


def add_functions_to_jinja2(current_app):
    """
    Ajoute les fonctions de data pour le templating avec jinja 2
    :param current_app: Application sur laquelle ajouter les fonctions
    """
    from application.passions import data as data_passions
    from application.portfolio import data as data_portfolio
    from application.apps import data as data_apps
    current_app.jinja_env.globals.update(passions_list=data_passions.passions)
    current_app.jinja_env.globals.update(portfolio_list=data_portfolio.projects)
    current_app.jinja_env.globals.update(apps_list=data_apps.app_list)


def set_all_logger_to_level(logging_level):
    """
    Set tous les logger au niveau donné
    Note : Utiliser cette fonction essentiellement pour le mode debug, afin d'éviter de modifier le fichier YAML
    :param logging_level: Le niveau de logs souhaité
    """
    # Todo -> Ajouter les nouveaux loggers ici pour le mode debug
    from application.apps.webcrawler import logger as logger_webcrawler
    from application.apps.stringToLeet import logger as logger_string_to_leet
    from application.apps.anagramos import logger as logger_anagramos
    logger_webcrawler.setLevel(logging_level)
    logger_string_to_leet.setLevel(logging_level)
    logger_anagramos.setLevel(logging_level)


# Creation de l'app
def create_app(config_class=DevelopmentConfig):
    """
    Creation de l'application
    :param config_class: Classe de configuration -> Default is DevelopmentConfig
    :return: The created app with all the information
    """
    # Doit être global pour permettre d'avoir accès au logger dans l'application
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')
    app.config.from_object(config_class)
    # db.init_app(app)
    # migrate.init_app(app, db)
    bootstrap.init_app(app)
    blueprint_registrations(app)
    add_functions_to_jinja2(app)
    assets_from_env = Environment(app)
    create_static_bundles_assets(assets_from_env)
    setup_logging()
    app.logger.debug("Init of app finished")
    if config_class == DevelopmentConfig:
        set_all_logger_to_level(logging.DEBUG)
    return app

# Ce from est ici pour éviter les inclusion circulaire
# from application import models
