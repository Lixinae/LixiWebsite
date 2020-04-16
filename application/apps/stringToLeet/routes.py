import concurrent.futures

from flask import render_template, make_response, request

from application.apps.stringToLeet import string_to_leet_bp


############################################
#                Apps                      #
############################################

@string_to_leet_bp.route('/string_to_leet', methods=['GET', 'POST'])
def string_to_leet():
    # Todo -> method == POST / GET
    if request.method == "POST":
        # Todo -> Rajouter la reception du formulaire
        phrase_to_translate = ""

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(string_to_leet, phrase_to_translate)
            translated_string = future.result()
            return make_response(render_template('stringToLeet.html', title="string_to_leet", translated_string=translated_string), 200)
    else:
        return make_response(render_template('stringToLeet.html', title="string_to_leet"), 200)
