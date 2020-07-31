from flask import Blueprint

acronymos_bp = Blueprint('acronymos_bp', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/apps/acronymos")

from backend.unused.acronymos import routes
