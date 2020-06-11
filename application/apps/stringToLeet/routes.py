import concurrent.futures

from flask import render_template, make_response, request, jsonify

from application.apps.stringToLeet import string_to_leet_api, stringToLeet_source
from flask_restx import Resource


############################################
#             String to leet               #
############################################

@string_to_leet_api.route('/')
class StringToLeetPage(Resource):
    def get(self):
        return make_response(render_template('stringToLeet.html', title="string_to_leet"), 200)

    def post(self):
        phrase = request.form['phrase']
        if not phrase:
            return make_response(render_template('stringToLeet.html', title="string_to_leet", error="No word in input"), 200)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(stringToLeet_source.string_to_leet, phrase)
            phrase_translated = future.result()
            # Todo -> Utiliser l'ajax coté client et faire la réponse
            return jsonify({"results": phrase_translated})
