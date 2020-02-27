from flask import render_template, make_response

from application.index import index_bp


############################################
#             Index                        #
############################################

@index_bp.route('/')
@index_bp.route('/index')
def index():
    return make_response(render_template('index.html', title="Home"), 200)
