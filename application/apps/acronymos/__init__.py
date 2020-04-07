from flask import Blueprint

acronymos_bp = Blueprint('acronymos_bp', __name__,
                         static_folder='static',
                         template_folder='templates')

from application.apps.acronymos import routes
