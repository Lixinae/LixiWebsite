from flask import render_template, make_response, jsonify

from application.apps.pendu import pendu_api, pendu_bp
from application.apps.common_data import apps_toolbox
from flask_restx import Resource
import concurrent.futures


############################################
#              Pendu Page                  #
############################################

@pendu_bp.route("/")
def pendu_page():
    return make_response(render_template('Pendu_app.html', title="Pendu"), 200)


############################################
#              Pendu API                   #
############################################

@pendu_api.route('/updateParameters')
class PenduApiUpdateParameters(Resource):
    def get(self):
        # Todo
        pass

    def post(self):
        # Todo PenduApiUpdateParameters Post
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu_app.html', title="Pendu", error=error_message), 400)


@pendu_api.route('/restartGame')
class PenduApiRestartGame(Resource):
    def get(self):
        # Todo
        pass

    def post(self):
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu_app.html', title="Pendu", error=error_message), 400)


@pendu_api.route('/sendLetter')
class PenduApi(Resource):

    def __init(self):
        self.numb_attempts_left = 8  # Todo rendre ça paramétrable avec une requête post
        self.already_tried_letters = []

    def post(self):
        received_letter = ""

        # Todo Ajouter le check de la lettre reçu
        letter_ok = True

        return jsonify({"is_letter_ok": letter_ok,
                        "numb_attempts_left": self.numb_attempts_left,
                        "already_tried_letters": self.already_tried_letters})

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu_app.html', title="Pendu", error=error_message), 400)
