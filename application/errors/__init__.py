from flask import Blueprint

errors_bp = Blueprint('errors_bp', __name__,
                      static_folder='static',
                      template_folder='templates')

from application.errors import routes
