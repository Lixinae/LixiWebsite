from flask import render_template, make_response

from application.errors import bp


############################################
#             Erreur 404                   #
############################################

@bp.errorhandler(404)
def notfound():
    return make_response(render_template("errors/404.html"), 404)
