from flask import render_template, make_response

from backend.contact import contact_bp


############################################
#             Contact                      #
############################################

@contact_bp.route('/contact')
def contact():
    return make_response(render_template('contact.html', title="Contact"), 200)
