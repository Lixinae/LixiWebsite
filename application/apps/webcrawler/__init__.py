from flask import Blueprint
import logging

logger = logging.getLogger('VahenWebsite.apps.webcrawler')

webcrawler_bp = Blueprint('webcrawler_bp', __name__,
                          static_folder='static',
                          template_folder='templates',
                          url_prefix="/apps/webcrawler")

from application.apps.webcrawler import routes
