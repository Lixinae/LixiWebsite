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
        if request.method == "GET":
            return make_response(render_template('anagramos.html', title="Anagramos"), 200)

    def post(self):
        if request.method == "POST":
            """
            Dans la requete "POST" on récupère les du formulaire
            Champs : 'word', 'language-select'
            """
            word = request.form['word']
            lang = request.form['language-select']
            words = []
            if lang == "French":
                words = apps_toolbox.get_french_words()
            elif lang == "English":
                words = apps_toolbox.get_english_words()
            if not words:
                return make_response(render_template('anagramos.html', title="Anagramos", error="No language selected"), 200)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(anagramos_source.find_anagrammes, word, words)
                output_word_list = future.result()
                # On ne veut pas donner le mot dont on cherche les anagrames
                if word in output_word_list:
                    output_word_list.remove(word)
            if output_word_list:
                return jsonify({"results": output_word_list})
