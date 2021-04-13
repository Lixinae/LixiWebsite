from flask import render_template, make_response, request, jsonify
from flask_restx import Resource

from application.passions.travail_du_cuir_api import travail_du_cuir_bp, travail_du_cuir_api


############################################
#          Travail du cuir Route           #
############################################
@travail_du_cuir_bp.route('/')
def travail_du_cuir_page():
    return make_response(render_template('passions/travail_du_cuir/travail_du_cuir.html', title="travail_du_cuir"), 200)


@travail_du_cuir_bp.route('/accessoires')
def travail_du_cuir_accessoires():
    return make_response(render_template('passions/travail_du_cuir/travail_du_cuir_accessoires.html',
                                         title="travail_du_cuir_accessoires"), 200)


@travail_du_cuir_bp.route('/canons')
def travail_du_cuir_canons():
    return make_response(
        render_template('passions/travail_du_cuir/travail_du_cuir_canons.html', title="travail_du_cuir_canons"), 200)


@travail_du_cuir_bp.route('/bracelets')
def travail_du_cuir_petit_bracelets():
    return make_response(
        render_template('passions/travail_du_cuir/travail_du_cuir_bracelets.html', title="travail_du_cuir_bracelets"),
        200)


@travail_du_cuir_bp.route('/motifs')
def travail_du_cuir_motifs():
    return make_response(
        render_template('passions/travail_du_cuir/travail_du_cuir_motifs.html', title="travail_du_cuir_motifs"), 200)


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
