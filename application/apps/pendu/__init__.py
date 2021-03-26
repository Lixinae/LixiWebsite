import logging

from flask import Blueprint
from flask_restx import Api
from application.configuration import web_templates_dir, web_static_dir
from application.apps import apps_folder

logger = logging.getLogger("VahenWebsite.apps.pendu")

pendu_bp = Blueprint('pendu_bp', __name__,
                     static_folder=web_static_dir + apps_folder + '/pendu',
                     template_folder=web_templates_dir + apps_folder + '/pendu',
                     url_prefix="/apps/pendu")

pendu_api = Api(pendu_bp, version="1.0", title="Pendu API", description="The API for the pendu app", prefix="/api")

from application.apps.pendu import routes
