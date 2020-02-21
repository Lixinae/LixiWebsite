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
# Ce from est ici pour éviter les inclusion circulaire
from application import routes, models
