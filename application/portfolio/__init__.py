from flask import Blueprint
from application.configuration import web_templates_dir, web_static_dir

portfolio_bp = Blueprint('portfolio_bp', __name__,
                         static_folder=web_static_dir + '/portfolio',
                         template_folder=web_templates_dir + '/portfolio',
                         url_prefix="/portfolio")

from application.portfolio import routes
