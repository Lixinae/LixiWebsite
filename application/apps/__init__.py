from flask import Blueprint
from application.configuration import web_templates_dir, web_static_dir
import logging

logger = logging.getLogger('VahenWebsite.apps')
apps_folder = "/apps"

apps_bp = Blueprint('apps_bp', __name__,
                    static_folder=web_static_dir + apps_folder,
                    template_folder=web_templates_dir + apps_folder,
                    url_prefix=apps_folder)

from application.apps import routes
