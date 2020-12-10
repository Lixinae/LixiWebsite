from flask import Blueprint
from application.configuration import web_templates_dir, web_static_dir

games_bp = Blueprint('games_bp', __name__,
                     static_folder=web_static_dir + '/games',
                     template_folder=web_templates_dir + '/games')

from application.games import routes
