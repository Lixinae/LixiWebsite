from flask import render_template, make_response

from application.portfolio import data, portfolio_bp


############################################
#             Portfolio                    #
############################################

# Les routes ont pour prefix : url_prefix="/portfolio"

@portfolio_bp.route('/')
def portfolio():
    project_m = data.projects()
    return make_response(render_template('portfolio.html', title="Portfolio", projectList=project_m), 200)


@portfolio_bp.route('/sitePerso')
def portfolio_site_perso():
    return make_response(render_template('./portfolio/sitePerso.html', title="sitePerso"), 200)


@portfolio_bp.route('/pacman3d')
def portfolio_pacman3d():
    return make_response(render_template('./portfolio/pacman3d.html', title="Pacmand 3D"), 200)


@portfolio_bp.route('/webcrawler')
def portfolio_webcrawler():
    return make_response(render_template('./portfolio/webcrawler.html', title="WebCrawler"), 200)


@portfolio_bp.route('/raytracer')
def portfolio_raytracer():
    return make_response(render_template('./portfolio/raytracer.html', title="Raytracer"), 200)


@portfolio_bp.route('/plateforme_game')
def portfolio_plateforme_game():
    return make_response(render_template('./portfolio/plateforme_game.html', title="Plateforme Game"), 200)


@portfolio_bp.route('/runner')
def portfolio_runner():
    return make_response(render_template('./portfolio/runner.html', title="Runner"), 200)
