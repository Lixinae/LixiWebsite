import logging

from flask import Blueprint
from flask_restx import Api
from application.configuration import web_templates_dir, web_static_dir

logger = logging.getLogger("VahenWebsite.passions.travail_du_cuir")
travail_du_cuir_static_folder = web_static_dir + '/passions/travail_du_cuir'
travail_du_cuir_template_folder = web_templates_dir + '/passions/travail_du_cuir'

travail_du_cuir_bp = Blueprint('travail_du_cuir_bp', __name__,
                               static_folder=travail_du_cuir_static_folder,
                               template_folder=travail_du_cuir_template_folder,
                               url_prefix="/passions/travail_du_cuir")

travail_du_cuir_api = Api(travail_du_cuir_bp,
                          version="1.0",
                          title="Leatherwork API",
                          description="Cette API permet de récupérer les informations sur travail du cuir",
                          prefix="/api")

from application.passions.travail_du_cuir_api import routes
