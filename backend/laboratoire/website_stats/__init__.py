from flask import Blueprint
import logging

logger = logging.getLogger('VahenWebsite.laboratoire.website_stats')

website_stats_bp = Blueprint('website_stats_bp', __name__,
                             static_folder='static',
                             template_folder='templates',
                             url_prefix="/laboratoire/website_stats")

from backend.laboratoire.website_stats import routes
