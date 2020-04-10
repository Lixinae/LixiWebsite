from flask import Blueprint

anagramos_bp = Blueprint('anagramos_bp', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/apps")

from application.apps.anagramos import routes
