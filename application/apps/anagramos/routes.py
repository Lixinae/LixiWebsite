from flask import render_template, make_response, request

from application.apps.anagramos import anagramos_bp, anagramos_source
from application.apps.common_data import apps_toolbox

import concurrent.futures


############################################
#                Anagramos                 #
############################################

@anagramos_bp.route('/anagramos', methods=['GET', 'POST'])
def anagramos():
    if request.method == "POST":
        word = request.form['word']

        lang = request.form['language-select']
        words = []
        if lang == "French":  # language_enum.Language.FRENCH:
            words = apps_toolbox.get_french_words()
        elif lang == "English":  # language_enum.Language.ENGLISH:
            words = apps_toolbox.get_english_words()
        if not words:
            return make_response(render_template('anagramos.html', title="Anagramos", error="No language selected"), 200)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(anagramos_source.find_anagrammes, word, words)
            output_word_list = future.result()
            return make_response(render_template('anagramos.html', title="Anagramos", results=output_word_list, word=word), 200)
    else:
        return make_response(render_template('anagramos.html', title="Anagramos"), 200)
