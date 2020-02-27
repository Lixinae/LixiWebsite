from flask import Blueprint

bp = Blueprint('portfolio', __name__)

from application.portfolio import routes
