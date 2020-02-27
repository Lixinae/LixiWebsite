from flask import render_template, make_response
from application import app


@app.route('/')
@app.route('/index')
def index():
    return make_response(render_template('index.html', title="Home"), 200)


############################################
#             About                        #
############################################

@app.route('/about')
def about():
    # Todo -> Add data if needed
    return make_response(render_template('about.html'), 200)


############################################
#             Contact                      #
############################################

@app.route('/contact')
def contact():
    return make_response(render_template('contact.html', title="Contact"), 200)


############################################
#             Erreur 404                   #
############################################

@app.errorhandler(404)
def notfound():
    return make_response(render_template("errors/404.html"), 404)
