from flask import render_template, make_response

from application.apps import apps_bp
from application.apps.data import app_list
from application.database.models.app_model import App


############################################
#                Apps                      #
############################################

@apps_bp.route('/')
def apps():
    return make_response(render_template('apps.html', title="Apps", app_list=app_list()), 200)


# Todo -> Utilisé quand la BDD sera opérationnel
# def app_list():
#     applications = App.query.all()
#     return applications
