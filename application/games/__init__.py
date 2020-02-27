from flask import Blueprint

bp = Blueprint('games', __name__)

from application.games import routes
