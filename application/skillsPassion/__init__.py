from flask import Blueprint

skills_passion_bp = Blueprint('skills_passion_bp', __name__,
                              static_folder='static',
                              template_folder='templates')

from application.skillsPassion import routes
