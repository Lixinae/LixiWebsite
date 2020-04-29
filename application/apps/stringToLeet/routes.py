import concurrent.futures

from flask import render_template, make_response, request

from application.apps.stringToLeet import string_to_leet_bp, stringToLeet_source


############################################
#             String to leet               #
############################################

@string_to_leet_bp.route('/string_to_leet', methods=['GET', 'POST'])
def string_to_leet():
    # Todo -> method == POST / GET
    if request.method == "POST":
        phrase = request.form['phrase']
        if not phrase:
            return make_response(render_template('anagramos.html', title="Anagramos", error="No word in input"), 200)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(stringToLeet_source.string_to_leet, phrase)
            phrase_translated = future.result()
            return make_response(render_template('stringToLeet.html',
                                                 title="string_to_leet",
                                                 phrase=phrase,
                                                 phrase_translated=phrase_translated),
                                 200)
    else:
        return make_response(render_template('stringToLeet.html', title="string_to_leet"), 200)
