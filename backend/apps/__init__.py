from flask import Blueprint
import logging

logger = logging.getLogger('VahenWebsite.apps')

apps_bp = Blueprint('apps_bp', __name__,
                    static_folder='static',
                    template_folder='templates',
                    url_prefix="/apps")

from backend.apps import routes
