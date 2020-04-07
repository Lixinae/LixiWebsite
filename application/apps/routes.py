from flask import render_template, make_response

from application.apps import apps_bp

from application.passions import data as data_passions
from application.portfolio import data as data_portfolio

from application.apps.data import app_list


############################################
#                Apps                      #
############################################

@apps_bp.route('/apps')
def apps():
    apps_list = app_list()
    return make_response(render_template('apps.html', title="Home", apps_list=apps_list), 200)
