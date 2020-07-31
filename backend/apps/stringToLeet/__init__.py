import logging

from flask import Blueprint
from flask_restx import Api

logger = logging.getLogger("VahenWebsite.apps.stringToLeet")

string_to_leet_bp = Blueprint('string_to_leet_bp', __name__,
                              static_folder='static',
                              template_folder='templates',
                              url_prefix="/apps/string_to_leet")

string_to_leet_api = Api(string_to_leet_bp, version="1.0", title="String to Leet API", description="The API for the String to leet app", )

from backend.apps.stringToLeet import routes
