from flask import Blueprint

games_bp = Blueprint('games_bp', __name__,
                     static_folder='static',
                     template_folder='templates')

from application.games import routes
