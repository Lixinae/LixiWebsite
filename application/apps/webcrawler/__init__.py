from flask import Blueprint
import logging
from flask_restx import Api
from application.configuration import web_templates_dir, web_static_dir
from application.apps import apps_folder
logger = logging.getLogger('VahenWebsite.apps.webcrawler')

webcrawler_bp = Blueprint('webcrawler_bp', __name__,
                          static_folder=web_static_dir + apps_folder + '/webcrawler',
                          template_folder=web_templates_dir + apps_folder + '/webcrawler',
                          url_prefix="/apps/webcrawler")

webcrawler_api = Api(webcrawler_bp, version="1.0", title="Webcrawler API", description="The API for the webcrawler app", )

from application.apps.webcrawler import routes
