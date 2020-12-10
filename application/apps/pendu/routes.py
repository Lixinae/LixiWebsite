from flask import render_template, make_response, request, jsonify

from application.apps.pendu import pendu_api
from application.apps.common_data import apps_toolbox
from flask_restx import Resource
import concurrent.futures


############################################
#                Pendu                     #
############################################

@pendu_api.route('/updateParameters')
class PenduPageUpdateParameters(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu.html', title="Pendu", error=error_message), 400)

@pendu_api.route('/restartGame')
class PenduPageRestartGame(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu.html', title="Pendu", error=error_message), 400)

@pendu_api.route('/')
class PenduPage(Resource):

    def __init(self):
        self.numb_attempts_left = 8 # Todo rendre ça paramétrable avec une requête post
        self.already_tried_letters = []

    def get(self):
        return make_response(render_template('Pendu.html', title="Pendu"), 200)

    def post(self):

        received_letter = ""

        # Todo Ajouter le check de la lettre reçu
        letter_ok = True

        return jsonify({"is_letter_ok": letter_ok,
                        "numb_attempts_left" : self.numb_attempts_left,
                        "already_tried_letters": self.already_tried_letters})

    def error_template(self, error_message: str):
        return make_response(render_template('Pendu.html', title="Pendu", error=error_message), 400)