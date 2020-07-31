from flask import Blueprint

portfolio_bp = Blueprint('portfolio_bp', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/portfolio")

from backend.portfolio import routes
