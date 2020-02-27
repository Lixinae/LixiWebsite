from flask import render_template, make_response
from application import app
from application.portfolio import data


@app.route('/')
@app.route('/index')
def index():
    return make_response(render_template('index.html', title="Home"), 200)


############################################
#             Portfolio                    #
############################################

# Todo -> Rajouter une route pour chaque projets plus en détail

@app.route('/portfolio')
def portfolio():
    project_m = data.projects()
    return make_response(render_template('portfolio.html', title="Portfolio", projects=project_m), 200)


@app.route('/portfolio/sitePerso')
def portfolio_site_perso():
    project = data.projects()[1]
    return make_response(render_template('./portfolio/sitePerso.html', title="sitePerso", project=project), 200)


@app.route('/portfolio/pacman3d')
def portfolio_pacman3d():
    project = data.projects()[0]
    return make_response(render_template('./portfolio/pacman3d.html', title="Pacmand 3D", project=project), 200)


@app.route('/portfolio/webcrawler')
def portfolio_webcrawler():
    project = data.project_specific()
    return make_response(render_template('./portfolio/webcrawler.html', title="WebCrawler", project=project), 200)


@app.route('/portfolio/raytracer')
def portfolio_raytracer():
    project = data.project_specific()
    return make_response(render_template('./portfolio/raytracer.html', title="Raytracer", project=project), 200)


@app.route('/portfolio/plateforme_game')
def portfolio_plateforme_game():
    project = data.project_specific()
    return make_response(render_template('./portfolio/plateforme_game.html', title="Plateforme Game", project=project), 200)


@app.route('/portfolio/runner')
def portfolio_runner():
    project = data.project_specific()
    return make_response(render_template('./portfolio/runner.html', title="Runner", project=project), 200)


############################################
#             Skills Passion               #
############################################

@app.route('/skillsPassion')
def skills_passion():
    return make_response(render_template('skillsPassion.html', title="skillsPassion"), 200)


@app.route('/skillsPassion/GN')
def skills_passion_gn():
    return make_response(render_template('./skillsPassion/gn.html', title="GN"), 200)


@app.route('/skillsPassion/TravailDuCuir')
def skills_passion_travail_du_cuir():
    return make_response(render_template('./skillsPassion/travailDuCuir.html', title="Travail du cuir"), 200)


@app.route('/skillsPassion/JeuxDeSociete')
def skills_passion_jeux_de_societe():
    return make_response(render_template('./skillsPassion/jeuxDeSociete.html', title="Jeux de sociéte"), 200)


@app.route('/skillsPassion/JeuxDeRole')
def skills_passion_jeux_de_role():
    return make_response(render_template('./skillsPassion/jeuxDeRole.html', title="Jeux de rôle"), 200)


@app.route('/skillsPassion/serveurMultimedia')
def skills_passion_serveur_multimedia():
    return make_response(render_template('./skillsPassion/serveurMultimedia.html', title="Serveur multimedia"), 200)

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
