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
        post_data = request.get_json()
        if post_data is None:
            return self.error_template("No data received")
        if 'phrase' not in post_data:
            return self.error_template("Json is incorrect")
        phrase = post_data['phrase']
        if not phrase:
            return self.error_template("No word in input")
        # Todo -> Later replace with celery task
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(stringToLeet_source.string_to_leet, phrase)
            phrase_translated = future.result()
            return jsonify({"results": phrase_translated})

    def error_template(self, error_message: str):
        return make_response(render_template('stringToLeet.html', title="string_to_leet", error=error_message), 400)
