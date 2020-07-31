from flask import render_template, make_response

from backend.laboratoire import laboratoire_bp

from backend.laboratoire.data import laboratoire_list


############################################
#                Apps                      #
############################################

@laboratoire_bp.route('/')
def apps():
    return make_response(render_template('laboratoire.html', title="Laboratoire", laboratoire_list=laboratoire_list()), 200)
