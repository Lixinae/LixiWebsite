from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from application.configuration import Configuration

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)


# Enregistrement des blueprint
def blueprint_registrations(current_app):
    # from application.about import bp as about_bp
    # from application.contact import bp as contact_bp
    # from application.errors import bp as errors_bp
    from application.portfolio import portfolio_bp
    from application.skillsPassion import skills_passion_bp
    # current_app.register_blueprint(about_bp)
    # current_app.register_blueprint(contact_bp)
    # current_app.register_blueprint(errors_bp)
    current_app.register_blueprint(portfolio_bp)
    current_app.register_blueprint(skills_passion_bp)


blueprint_registrations(app)
# Creation de l'app
# def create_app(config_class=Configuration):
#     app = Flask(__name__,
#                 static_folder='static',
#                 template_folder='templates')
#     app.config.from_object(config_class)
#     db.init_app(app)
#     migrate.init_app(app, db)
#     bootstrap.init_app(app)
#     blueprint_registrations(app)
#     return app


# Ce from est ici pour éviter les inclusion circulaire
from application import routes, models
