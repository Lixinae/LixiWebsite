from flask import Blueprint

string_to_leet_bp = Blueprint('string_to_leet_bp', __name__,
                              static_folder='static',
                              template_folder='templates')

from application.apps.stringToLeet import routes
