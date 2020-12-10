from flask import Blueprint
from application.configuration import web_templates_dir, web_static_dir
errors_bp = Blueprint('errors_bp', __name__,
                      static_folder='static',
                      template_folder='templates',
                      url_prefix="/errors")

from application.errors import routes
