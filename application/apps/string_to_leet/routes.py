import concurrent.futures

from flask import render_template, make_response, request, jsonify
from flask_restx import Resource

from application.apps.string_to_leet import string_to_leet_api, string_to_leet_source, string_to_leet_bp


############################################
#           String to leet Route           #
############################################

@string_to_leet_bp.route('/')
def string_to_leet_page():
    return make_response(render_template('string_to_leet_app.html', title="string_to_leet"), 200)


############################################
#            String to leet API            #
############################################

@string_to_leet_api.route('/translateToLeet')
class StringToLeetApi(Resource):
    def get(self):
        data = request.args.to_dict()
        if data is None:
            return self.error_template("No data received")
        if 'phrase' not in data:
            return self.error_template("Json is incorrect")
        phrase = data['phrase']
        if not phrase:
            return self.error_template("No word in input")
        # Todo -> Later replace with celery task
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(string_to_leet_source.string_to_leet, phrase)
            phrase_translated = future.result()
            return jsonify({"results": phrase_translated})

    def post(self):
        pass

    @staticmethod
    def error_template(error_message: str):
        return make_response(render_template('string_to_leet_app.html', title="string_to_leet", error=error_message),
                             400)
