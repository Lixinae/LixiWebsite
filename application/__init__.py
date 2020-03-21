from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
from flask_bootstrap import Bootstrap

from application.configuration import Configuration, DevelopmentConfig

# db = SQLAlchemy()
# migrate = Migrate()
bootstrap = Bootstrap()


# Enregistrement des blueprint
def blueprint_registrations(current_app):
    # from application.cv import cv_bp
    from application.index import index_bp
    # from application.contact import contact_bp
    from application.errors import errors_bp
    from application.portfolio import portfolio_bp
    from application.passions import passions_bp
    from application.webcrawler import webcrawler_bp
    current_app.register_blueprint(index_bp)
    # current_app.register_blueprint(cv_bp)
    # current_app.register_blueprint(contact_bp)
    current_app.register_blueprint(errors_bp)
    current_app.register_blueprint(portfolio_bp)
    current_app.register_blueprint(passions_bp)
    current_app.register_blueprint(webcrawler_bp)


# Creation de l'app
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')
    app.config.from_object(config_class)
    # db.init_app(app)
    # migrate.init_app(app, db)
    bootstrap.init_app(app)
    blueprint_registrations(app)
    return app


# Ce from est ici pour éviter les inclusion circulaire
from application import models
