import logging

from flask import Blueprint
from flask_restx import Api
from application.configuration import web_templates_dir, web_static_dir
from application.apps import apps_folder

logger = logging.getLogger("VahenWebsite.apps.anagramos")

anagramos_bp = Blueprint('anagramos_bp', __name__,
                         static_folder=web_static_dir + apps_folder + '/anagramos',
                         template_folder=web_templates_dir + apps_folder + '/anagramos',
                         url_prefix="/apps/anagramos")

anagramos_api = Api(anagramos_bp, version="1.0", title="Anagramos API", description="The API for the anagramos app", )

from application.apps.anagramos import routes
