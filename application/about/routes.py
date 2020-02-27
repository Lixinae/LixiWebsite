from flask import render_template, make_response

from application.about import about_bp


############################################
#             About                        #
############################################

@about_bp.route('/about')
def about():
    # Todo -> Add data if needed
    return make_response(render_template('about.html'), 200)
