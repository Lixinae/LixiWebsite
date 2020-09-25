from flask import render_template, make_response, request, jsonify

from application.apps.anagramos import anagramos_source, anagramos_api
from application.apps.common_data import apps_toolbox
from flask_restx import Resource
import concurrent.futures


############################################
#                Anagramos                 #
############################################

@anagramos_api.route('/')
class AnagramosPage(Resource):
    def get(self):
        return make_response(render_template('anagramos.html', title="Anagramos"), 200)

    def post(self):
        """
        Dans la requete "POST" on récupère les champs du formulaire
        Champs : 'word', 'language_select'
        """
        post_data = request.get_json()
        if post_data is None:
            return self.error_template("No data received")
        if "word" not in post_data or "language_select" not in post_data:
            return self.error_template("Json is incorrect")
        word = post_data["word"]
        lang = post_data["language_select"]
        words = []
        if lang == "French":
            words = apps_toolbox.get_french_words()
        elif lang == "English":
            words = apps_toolbox.get_english_words()
        if not words:
            return make_response(render_template('anagramos.html', title="Anagramos", error="No language selected"), 400)
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

    def error_template(self, error_message: str):
        return make_response(render_template('anagramos.html', title="Anagramos", error=error_message), 400)