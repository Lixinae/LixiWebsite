from flask import Blueprint

index_bp = Blueprint('index_bp', __name__,
                     static_folder='static',
                     template_folder='templates')

from application.index import routes
