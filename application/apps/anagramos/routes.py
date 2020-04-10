from flask import render_template, make_response, request

from application.apps.anagramos import anagramos_bp

import concurrent.futures


############################################
#                A                      #
############################################

@anagramos_bp.route('/anagramos', methods=['GET', 'POST'])
def anagramos():
    if request.method == "POST":
        # Todo -> Rajouter la reception du formulaire
        word = ""
        words = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(anagramos.find_anagrammes, word, words)
            output_word_list = future.result()
            return make_response(render_template('anagramos.html', title="Anagramos", words_list=output_word_list), 200)
    else:
        return make_response(render_template('anagramos.html', title="Anagramos"), 200)
