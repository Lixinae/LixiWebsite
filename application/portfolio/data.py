from typing import List, Dict

from flask import url_for
# from application import models


# Permet de query la liste de tous les projets
def projects() -> List[Dict]:
    projects_m = [
        {
            'name': "Vahen website",
            'outils': "Python 3,Flask, Docker, HTML5, CSS3, Bootstrap4, Jinja2",
            'quick_description': "Site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/miniature/sitePerso_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_site_perso')
        },
        {
            'name': "Webcrawler",
            'outils': "Python 3, Beautiful Soup 4",
            'quick_description': "Un webcrawler simple",
            'miniature': url_for('static', filename='img/miniature/webCrawler_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_webcrawler')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': "Un pacman en 3D",
            'miniature': url_for('static', filename='img/miniature/pacman_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_pacman3d')
        },
        {
            'name': "Runner",
            'outils': "Unity 3D, C#, Python 3",
            'quick_description': "",
            'miniature': url_for('static', filename='img/miniature/runner_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_runner')
        },
        {
            'name': "Plateforme Game",
            'outils': "Unity 3D, C#",
            'quick_description': "",
            'miniature': url_for('static', filename='img/miniature/plateforme_game_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_plateforme_game')
        },
        {
            'name': "Raytracer",
            'outils': "C++11, SDL2, CMake",
            'quick_description': "Un raytracer réalisé from scratch",
            'miniature': url_for('static', filename='img/miniature/raytracer_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_raytracer')
        },
    ]
    return projects_m


# Permet de query un projet en particulier
# Si l'on ne passe pas de projet -> Renvoie un dictionnaire vide
def project_specific(project_name="") -> Dict:
    if project_name == "":
        return {}
    for project in projects():
        if project['name'] == project_name:
            return project
    # project = models.Project.query.get_or_404(project_name)
    # return project.to_dict()
    return {}


def project_short() -> List[Dict]:
    projects_m = [
        {
            'name': "Vahen website",
            'outils': "Python 3,Flask, Docker, HTML5, CSS3, Bootstrap4, Jinja2",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/miniature/sitePerso_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_site_perso')
        },
        {
            'name': "Webcrawler",
            'outils': "Python 3, Beautiful Soup 4",
            'quick_description': "Un webcrawler simple",
            'miniature': url_for('static', filename='img/miniature/webCrawler_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_webcrawler')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/miniature/pacman_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_pacman3d')
        },
    ]
    return projects_m
