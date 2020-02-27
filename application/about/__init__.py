from flask import Blueprint

bp = Blueprint('about', __name__)

from application.about import routes
