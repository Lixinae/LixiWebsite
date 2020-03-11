from flask import render_template, make_response

from application.portfolio import data, portfolio_bp


############################################
#             Portfolio                    #
############################################

# Todo -> Rajouter une route pour chaque projets plus en détail

@portfolio_bp.route('/portfolio')
def portfolio():
    project_m = data.projects()
    return make_response(render_template('portfolio.html', title="Portfolio", projectList=project_m), 200)


@portfolio_bp.route('/portfolio/sitePerso')
def portfolio_site_perso():
    # project = data.project_specific("sitePerso")
    return make_response(render_template('./portfolio/sitePerso.html', title="sitePerso"), 200)


@portfolio_bp.route('/portfolio/pacman3d')
def portfolio_pacman3d():
    # project = data.project_specific('pacman3d')
    project = data.project_specific()
    return make_response(render_template('./portfolio/pacman3d.html', title="Pacmand 3D", project=project), 200)


@portfolio_bp.route('/portfolio/webcrawler')
def portfolio_webcrawler():
    # project = data.project_specific('webcrawler')
    project = data.project_specific()
    return make_response(render_template('./portfolio/webcrawler.html', title="WebCrawler", project=project), 200)


@portfolio_bp.route('/portfolio/raytracer')
def portfolio_raytracer():
    # project = data.project_specific('raytracer')
    project = data.project_specific()
    return make_response(render_template('./portfolio/raytracer.html', title="Raytracer", project=project), 200)


@portfolio_bp.route('/portfolio/plateforme_game')
def portfolio_plateforme_game():
    # project = data.project_specific('plateforme_game')
    project = data.project_specific()
    return make_response(render_template('./portfolio/plateforme_game.html', title="Plateforme Game", project=project), 200)


@portfolio_bp.route('/portfolio/runner')
def portfolio_runner():
    # project = data.project_specific('runner')
    project = data.project_specific()
    return make_response(render_template('./portfolio/runner.html', title="Runner", project=project), 200)
