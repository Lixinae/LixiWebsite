import concurrent.futures

from flask import render_template, make_response, request

from application.apps.acronymos import acronymos_bp


############################################
#                Apps                      #
############################################

@acronymos_bp.route('/acronymos', methods=['GET', 'POST'])
def acronymos():
    if request.method == "POST":
        # Todo -> Rajouter la reception du formulaire
        # Todo -> Faire correction des fonctions d'acronymos
        word = ""
        words = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(acronymos)
            output_word_list = future.result()
            return make_response(render_template('acronymos.html', title="Anagramos", words_list=output_word_list), 200)
    else:
        return make_response(render_template('acronymos.html', title="Anagramos"), 200)
