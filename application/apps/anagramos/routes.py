from flask import render_template, make_response, request, jsonify

from application.apps.anagramos import anagramos_source, anagramos_api, anagramos_bp
from application.apps.common_data import apps_toolbox
from flask_restx import Resource
import concurrent.futures


############################################
#             Anagramos Route              #
############################################

@anagramos_bp.route('/')
def anagramos_page():
    return make_response(render_template('anagramos_app.html', title="Anagramos"), 200)


############################################
#              Anagramos API               #
############################################

@anagramos_api.route('/askForAnagrams')
class AnagramosApi(Resource):
    def get(self):
        """
        Dans la requete "POST" on récupère les champs du formulaire
        Champs : 'word', 'language_select'
        """
        get_data = request.args.to_dict()
        if get_data is None:
            return self.error_template("No data received")
        if "word" not in get_data or "language_select" not in get_data:
            return self.error_template("Json is incorrect")
        word = get_data["word"]
        lang = get_data["language_select"]
        words = []
        if lang == "French":
            words = apps_toolbox.get_french_words()
        elif lang == "English":
            words = apps_toolbox.get_english_words()
        if not words:
            return self.error_template("No language selected")
        # Todo -> Later replace with celery task
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(anagramos_source.find_anagrammes, word, words)
            output_word_list = future.result()
            # On ne veut pas donner le mot dont on cherche les anagrames
            if word in output_word_list:
                output_word_list.remove(word)
        if output_word_list:
            return jsonify({"results": output_word_list})
        return jsonify({"results": []})

    def post(self):
        pass

    def error_template(self, error_message: str):
        return make_response(render_template('anagramos_app.html', title="Anagramos", error=error_message), 400)
