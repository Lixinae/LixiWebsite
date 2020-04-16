import concurrent.futures

from flask import render_template, make_response, request

from application.apps.acronymos import acronymos_bp
from application.apps.acronymos.language_enum import Language
from application.apps.common_data.apps_toolbox import get_words_from_file


############################################
#                Apps                      #
############################################

@acronymos_bp.route('/acronymos', methods=['GET', 'POST'])
def acronymos():
    if request.method == "POST":
        # Todo -> Rajouter la reception du formulaire
        # Todo -> Faire correction des fonctions d'acronymos
        phrase = ""
        language = Language.FRENCH  # Default is french
        if language == language.FRENCH:
            fname = ""
        elif language == language.ENGLISH:
            fname = ""
        else:
            fname = ""
        words = get_words_from_file(fname)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit()  # Todo -> Rajouter fonction a submit
            output_word_list = future.result()
            return make_response(render_template('acronymos.html', title="Acronymos", words_list=output_word_list), 200)
    else:
        return make_response(render_template('acronymos.html', title="Acronymos"), 200)
