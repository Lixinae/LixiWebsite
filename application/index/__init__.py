from flask import Blueprint
from application.configuration import web_static_dir, web_templates_dir

index_bp = Blueprint('index_bp', __name__,
                     static_folder=web_static_dir+'/static',
                     template_folder=web_templates_dir + '/index')

from application.index import routes
