import logging

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_assets import Environment
from flask_statistics import Statistics

from application.configuration import DevelopmentConfig, ProductionConfig, TestingConfig, web_templates_dir, web_static_dir
from application.assets import create_static_bundles_assets
from application.logger import setup_logging
from flask_sqlalchemy import SQLAlchemy
# Ajout du mimetype pour corriger erreur windows
import mimetypes

mimetypes.add_type('text/javascript', '.js')
bootstrap = Bootstrap()


# Enregistrement des blueprint
def blueprint_registrations(current_app):
    """
    Register the blueprints for the app
    :param current_app: The app we are using
    """

    # Index
    from application.index import index_bp
    current_app.register_blueprint(index_bp)

    # Errors
    from application.errors import errors_bp
    current_app.register_blueprint(errors_bp)

    # Portfolio
    from application.portfolio import portfolio_bp
    current_app.register_blueprint(portfolio_bp)

    # Passions
    from application.passions import passions_bp
    current_app.register_blueprint(passions_bp)

    # Apps
    from application.apps import apps_bp
    from application.apps.webcrawler import webcrawler_bp
    from application.apps.anagramos import anagramos_bp
    from application.apps.string_to_leet import string_to_leet_bp
    from application.apps.pendu import pendu_bp
    current_app.register_blueprint(apps_bp)
    current_app.register_blueprint(webcrawler_bp)
    current_app.register_blueprint(anagramos_bp)
    current_app.register_blueprint(string_to_leet_bp)
    current_app.register_blueprint(pendu_bp)

    # Laboratoire
    from application.laboratoire import laboratoire_bp
    from application.laboratoire.website_stats import website_stats_bp
    current_app.register_blueprint(laboratoire_bp)
    current_app.register_blueprint(website_stats_bp)


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
    from application.apps.string_to_leet import logger as logger_string_to_leet
    from application.apps.anagramos import logger as logger_anagramos
    logger_webcrawler.setLevel(logging_level)
    logger_string_to_leet.setLevel(logging_level)
    logger_anagramos.setLevel(logging_level)


db = SQLAlchemy()


# Creation de l'app
def create_app(config_class=DevelopmentConfig):
    global db
    global statistics
    """
    Creation de l'application
    :param config_class: Classe de configuration -> Default is DevelopmentConfig
    :return: The created app with all the information
    """
    # Doit être global pour permettre d'avoir accès au logger dans l'application
    app = Flask(__name__,
                static_folder=web_static_dir + '/',
                template_folder=web_templates_dir + '/')
    app.config.from_object(config_class)
    setup_logging(config_class)
    app.logger.debug("Logging set up finished ")
    db.init_app(app)

    app.app_context().push()  # this does the bindind

    # We need those import for the metadata for the database
    # Todo -> Here add import for each model for the database
    import application.apps.app_model
    import application.portfolio.project_model
    db.create_all()
    app.logger.debug("Database init finished")

    bootstrap.init_app(app)
    app.logger.debug("Bootstrap init finished")

    blueprint_registrations(app)
    app.logger.debug("Blueprint_registrations finished")

    add_functions_to_jinja2(app)
    app.logger.debug("add_functions_to_jinja2 finished")

    assets_from_env = Environment(app)
    create_static_bundles_assets(assets_from_env)
    app.logger.debug("create_static_bundles_assets finished")

    if not config_class == TestingConfig:
        # Do not load the stats if we are in unit test mod
        from application.statistics.Request import Request
        statistics = Statistics(app, db, Request)
        app.logger.debug("Init of app finished")
    if config_class == DevelopmentConfig:
        set_all_logger_to_level(logging.DEBUG)
    return app
