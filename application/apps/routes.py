from flask import render_template, make_response

from application.apps import apps_bp

from application.apps.data import app_list


############################################
#                Apps                      #
############################################

@apps_bp.route('/apps')
def apps():
    return make_response(render_template('apps.html', title="Apps", app_list=app_list()), 200)
