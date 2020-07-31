import logging

from flask import Blueprint
from flask_restx import Api

logger = logging.getLogger("VahenWebsite.apps.anagramos")

anagramos_bp = Blueprint('anagramos_bp', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/apps/anagramos")

anagramos_api = Api(anagramos_bp, version="1.0", title="Anagramos API", description="The API for the anagramos app", )

from backend.apps.anagramos import routes
