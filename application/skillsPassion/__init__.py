from flask import Blueprint

bp = Blueprint('skillsPassion', __name__)

from application.skillsPassion import routes
