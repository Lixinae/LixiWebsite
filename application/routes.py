from flask import render_template

from application import app


# from application.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # user_m = {'username': 'Miguel'}
    # post_m = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     },
    #     {
    #         'author': {'username': 'Missan'},
    #         'body': 'Gungan dis gutl!'
    #     },
    #     {
    #         'author': {'username': 'Chris'},
    #         'body': 'Work is soooo fucking boooooooring'
    #     }
    # ]
    # return render_template('index.html', title="Home", user=user_m, posts=post_m)
    return render_template('index.html', title="Home")


@app.route('/about')
def about_me():
    # Todo -> Add data if needed
    return render_template('about.html', title="About_me")


@app.route('/portfolio')
def centre_interet():
    # Todo -> Add data if needed
    return render_template('portfolio.html', title="Portfolio")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash("Login requested for user:{}, remember me={}".format(form.username.data, form.remember_me.data))
#         # url_for -> Remplace le index par /index
#         # Evite d'avoir le chemin en dur et permet un refactor plus simple
#         return redirect(url_for("index"))
#     return render_template('login.html', title='Sign In', form=form)
