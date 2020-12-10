from flask import Blueprint
from application.configuration import web_templates_dir, web_static_dir
passions_bp = Blueprint('passions_bp', __name__,
                        static_folder=web_static_dir+'/passions',
                        template_folder=web_templates_dir+'/passions',
                        url_prefix="/passions")

from application.passions import routes
