from flask import render_template, make_response

from application.apps.stringToLeet import string_to_leet_bp


############################################
#                Apps                      #
############################################

@string_to_leet_bp.route('/string_to_leet', methods=['GET', 'POST'])
def string_to_leet():
    # Todo -> method == POST / GET
    return make_response(render_template('stringToLeet.html', title="string_to_leet"), 200)
