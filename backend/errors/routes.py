from flask import render_template, make_response

from backend.errors import errors_bp


############################################
#             Erreur 404                   #
############################################

@errors_bp.errorhandler(404)
def notfound():
    return make_response(render_template("errors/404.html"), 404)
