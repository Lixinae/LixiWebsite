from flask import render_template, make_response

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
    return make_response(render_template('index.html', title="Home"), 200)


@app.route('/portfolio')
def centre_interet():
    # Todo -> Faire une mini BDD avec les differents projets et query les éléments ici
    project_m = [
        {
            'titre': "Pacman3D",
            'langages': "C++11, OpenGL3+",
            'images': []
        },
        {
            'titre': "Vahen website",
            'langages': "Python 3",
            'images': []
        },
        {
            'titre': "",
        },
    ]
    return make_response(render_template('portfolio.html', title="Portfolio", projects=project_m), 200)


@app.route('/skillsPassion')
def skills_passion():
    return make_response(render_template('skillsPassion.html', title="SkillsPassion"), 200)


@app.route('/skillsPassion/GN')
def skills_passion():
    return make_response(render_template('./SkillsPassion/gn.html', title="gn"), 200)


@app.route('/skillsPassion/jeuxSurTable')
def skills_passion():
    return make_response(render_template('./SkillsPassion/jeuxSurTable.html', title="Jeux sur table"), 200)


@app.route('/skillsPassion/serveurMultimedia')
def skills_passion():
    return make_response(render_template('./SkillsPassion/serveurMultimedia.html', title="Serveur multimedia"), 200)


@app.route('/about')
def about_me():
    # Todo -> Add data if needed
    return make_response(render_template('about.html', title="About_me"), 200)


@app.route('/contact')
def skills_passion():
    return make_response(render_template('contact.html', title="Contact"), 200)


@app.errorhandler(404)
def notfound():
    """Serve 404 template."""
    return make_response(render_template("404.html"), 404)

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash("Login requested for user:{}, remember me={}".format(form.username.data, form.remember_me.data))
#         # url_for -> Remplace le index par /index
#         # Evite d'avoir le chemin en dur et permet un refactor plus simple
#         return redirect(url_for("index"))
#     return render_template('login.html', title='Sign In', form=form)
