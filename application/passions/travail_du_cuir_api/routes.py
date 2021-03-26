import concurrent.futures

from flask import render_template, make_response, request, jsonify
from flask_restx import Resource

from application.passions.travail_du_cuir_api import travail_du_cuir_bp, travail_du_cuir_api


############################################
#          Travail du cuir Route           #
############################################

@travail_du_cuir_bp.route('/')
def travail_du_cuir_page():
    return make_response(render_template('passions/travail_du_cuir/travail_du_cuir.html', title="travail_du_cuir"), 200)


############################################
#           Travail du cuir API            #
############################################

@travail_du_cuir_api.route('/get_instagram_data')
class TravailDuCuirGetInstagramData(Resource):
    def get(self):
        # Todo -> Ici faire un appel à la BDD sur la table qui contient les données "Instagram"
        pass

    def post(self):
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('passions/travail_du_cuir/travail_du_cuir.html', title="travail_du_cuir",
                                             error=error_message),
                             400)
