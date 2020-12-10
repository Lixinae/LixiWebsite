from flask import Blueprint
import logging
from application.configuration import web_templates_dir, web_static_dir

logger = logging.getLogger('VahenWebsite.laboratoire')

laboratoire_bp = Blueprint('laboratoire_bp', __name__,
                           static_folder=web_static_dir + '/laboratoire',
                           template_folder=web_templates_dir + '/laboratoire',
                           url_prefix="/laboratoire")

from application.laboratoire import routes
