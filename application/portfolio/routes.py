from flask import render_template, make_response

from application.portfolio import data, portfolio_bp
from application.portfolio.data_folder import data_site_perso, data_pacman3d, data_webcrawler, data_plateforme_game, data_runner


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
    skills_back = data_site_perso.skills_back()
    skills_front = data_site_perso.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/sitePerso.html',
        title="Site personnel",
        skills_back=skills_back,
        skills_front=skills_front), 200)


@portfolio_bp.route('/pacman3d')
def portfolio_pacman3d():
    skills_back = data_pacman3d.skills_back()
    skills_front = data_pacman3d.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/pacman3d.html',
        title="Pacmand 3D",
        skills_back=skills_back,
        skills_front=skills_front), 200)


@portfolio_bp.route('/webcrawler')
def portfolio_webcrawler():
    skills_back = data_webcrawler.skills_back()
    skills_front = data_webcrawler.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/webcrawler.html',
        title="WebCrawler",
        skills_back=skills_back,
        skills_front=skills_front), 200)


@portfolio_bp.route('/raytracer')
def portfolio_raytracer():
    skills_back = data_webcrawler.skills_back()
    skills_front = data_webcrawler.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/raytracer.html',
        title="Raytracer",
        skills_back=skills_back,
        skills_front=skills_front), 200)


@portfolio_bp.route('/plateforme_game')
def portfolio_plateforme_game():
    skills_back = data_plateforme_game.skills_back()
    skills_front = data_plateforme_game.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/plateforme_game.html',
        title="Plateforme Game",
        skills_back=skills_back,
        skills_front=skills_front), 200)


@portfolio_bp.route('/runner')
def portfolio_runner():
    skills_back = data_runner.skills_back()
    skills_front = data_runner.skills_front()
    return make_response(render_template(
        template_name_or_list='./portfolio/runner.html',
        title="Runner",
        skills_back=skills_back,
        skills_front=skills_front), 200)
