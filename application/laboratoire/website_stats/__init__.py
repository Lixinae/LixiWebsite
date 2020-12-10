from flask import Blueprint
import logging
from application.configuration import web_templates_dir, web_static_dir

logger = logging.getLogger('VahenWebsite.laboratoire.website_stats')
# Todo -> Utiliser une variable pour le /laboratoire
website_stats_bp = Blueprint('website_stats_bp', __name__,
                             static_folder=web_static_dir + '/laboratoire' + '/website_stats',
                             template_folder= web_templates_dir + '/laboratoire' + '/website_stats',
                             url_prefix="/laboratoire/website_stats")

from application.laboratoire.website_stats import routes
