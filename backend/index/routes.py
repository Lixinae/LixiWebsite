from flask import render_template, make_response

from backend.index import index_bp, data

from backend.passions import data as data_passions
from backend.portfolio import data as data_portfolio


############################################
#             Index                        #
############################################

@index_bp.route('/')
@index_bp.route('/index')
def index():
    passions_list = data_passions.passions_short()
    project_list = data_portfolio.project_short()
    skills_list = data.skills()
    return make_response(
        render_template('index.html', title="Home", passionsList=passions_list, projectList=project_list, skills=skills_list), 200)
