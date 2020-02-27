from flask import render_template, make_response

from application.contact import bp


############################################
#             Contact                      #
############################################

@bp.route('/contact')
def contact():
    return make_response(render_template('contact.html', title="Contact"), 200)
