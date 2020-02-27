from flask import render_template, make_response

from application.about import bp


############################################
#             About                        #
############################################

@bp.route('/about')
def about():
    # Todo -> Add data if needed
    return make_response(render_template('about.html'), 200)
