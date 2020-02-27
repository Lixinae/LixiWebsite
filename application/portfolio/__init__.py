from flask import Blueprint

portfolio_bp = Blueprint('portfolio_bp', __name__,
                         static_folder='static',
                         template_folder='templates')

from application.portfolio import routes
