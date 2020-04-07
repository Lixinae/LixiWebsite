from flask import render_template, make_response

from application.apps.acronymos import acronymos_bp


############################################
#                Apps                      #
############################################

@acronymos_bp.route('/acronymos')
def acronymos():
    return make_response(render_template('acronymos.html', title="Acronymos"), 200)
