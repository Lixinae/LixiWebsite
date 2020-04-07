from flask import render_template, make_response

from application.apps.stringToLeet import string_to_leet_bp


############################################
#                Apps                      #
############################################


@string_to_leet_bp.route('/stringToLeet')
def string_to_leet():
    return make_response(render_template('stringToLeet.html', title="stringToLeet"), 200)
