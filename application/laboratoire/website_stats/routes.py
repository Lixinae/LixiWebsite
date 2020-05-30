from flask import render_template, make_response

from application.laboratoire import laboratoire_bp

from application.laboratoire.data import laboratoire_list


############################################
#                Apps                      #
############################################

@laboratoire_bp.route('/')
def apps():
    return make_response(render_template('website_stats.html', title="Website_stats", laboratoire_list=laboratoire_list()), 200)
