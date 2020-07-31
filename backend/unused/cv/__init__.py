from flask import Blueprint

cv_bp = Blueprint('cv_bp', __name__,
                  static_folder='static',
                  template_folder='templates')

from backend.cv import routes
