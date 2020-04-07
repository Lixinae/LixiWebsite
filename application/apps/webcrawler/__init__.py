from flask import Blueprint

webcrawler_bp = Blueprint('webcrawler_bp', __name__,
                          static_folder='static',
                          template_folder='templates')

from application.apps.webcrawler import routes
