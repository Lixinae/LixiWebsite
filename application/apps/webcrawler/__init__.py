from flask import Blueprint
import logging
from flask_restx import Api

logger = logging.getLogger('VahenWebsite.apps.webcrawler')

webcrawler_bp = Blueprint('webcrawler_bp', __name__,
                          static_folder='static',
                          template_folder='templates',
                          url_prefix="/apps/webcrawler")

webcrawler_api = Api(webcrawler_bp, version="1.0", title="Webcrawler API", description="The API for the webcrawler app", )

from application.apps.webcrawler import routes
