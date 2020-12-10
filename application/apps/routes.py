from flask import render_template, make_response

from application.apps import apps_bp
from database_folder.models.app_model import App


############################################
#                Apps                      #
############################################

@apps_bp.route('/')
def apps():
    return make_response(render_template('apps.html', title="Apps", app_list=app_list()), 200)


def app_list():
    applications = App.query.all()
    return applications
