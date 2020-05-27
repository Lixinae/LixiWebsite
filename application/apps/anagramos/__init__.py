import logging

from flask import Blueprint

logger = logging.getLogger("VahenWebsite.apps.anagramos")

anagramos_bp = Blueprint('anagramos_bp', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/apps/anagramos")

from application.apps.anagramos import routes
