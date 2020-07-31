from flask import Blueprint

passions_bp = Blueprint('passions_bp', __name__,
                        static_folder='static',
                        template_folder='templates',
                        url_prefix="/passions")

from backend.passions import routes
