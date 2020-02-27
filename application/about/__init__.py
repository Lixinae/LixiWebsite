from flask import Blueprint

about_bp = Blueprint('about_bp', __name__,
                     static_folder='static',
                     template_folder='templates')

from application.about import routes
