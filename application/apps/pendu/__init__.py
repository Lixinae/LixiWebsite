import logging

from flask import Blueprint
from flask_restx import Api

logger = logging.getLogger("VahenWebsite.apps.pendu")

pendu_bp = Blueprint('pendu_bp', __name__,
                     static_folder='static',
                     template_folder='templates',
                     url_prefix="/apps/pendu")

pendu_api = Api(pendu_bp, version="1.0", title="Pendu API", description="The API for the pendu app", )

from application.apps.pendu import routes
