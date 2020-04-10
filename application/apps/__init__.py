from flask import Blueprint

apps_bp = Blueprint('apps_bp', __name__,
                    static_folder='static',
                    template_folder='templates',
                    url_prefix="/apps")

from application.apps import routes
