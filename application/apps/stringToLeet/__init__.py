from flask import Blueprint

string_to_leet_bp = Blueprint('string_to_leet_bp', __name__,
                              static_folder='static',
                              template_folder='templates',
                              url_prefix="/apps/string_to_leet")

from application.apps.stringToLeet import routes
