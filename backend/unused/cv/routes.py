from flask import render_template, make_response

from backend.cv import cv_bp


############################################
#             cv                        #
############################################

@cv_bp.route('/cv')
def cv():
    return make_response(render_template('cv.html'), 200)
