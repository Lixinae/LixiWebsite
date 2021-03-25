from typing import List, Dict

from flask import url_for


# from application import models


# Permet de query la liste de tous les projets
def projects() -> List[Dict]:
    projects_m = [
        {
            'name': "Vahen website",
            'outils': "Python 3, Flask, VueJs, HTML5, CSS3, JQuery, Bootstrap4, Jinja2, Docker",
            'quick_description': "Site personnel réalisé avec Python 3 / Flask / VueJs",
            'miniature': url_for('static', filename='general/img/miniature/site_perso_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_vahen_website'),
            'type': "Personnel"
        },
        {
            'name': "Webcrawler",
            'outils': "Python 3, Beautiful Soup 4",
            'quick_description': "Un webcrawler simple",
            'miniature': url_for('static', filename='general/img/miniature/webcrawler_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_webcrawler'),
            'type': "Personnel"
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': "Un pacman en 3D",
            'miniature': url_for('static', filename='general/img/miniature/pacman_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_pacman3d'),
            'type': "Universitaire"
        },
        # {
        #     'name': "Runner",
        #     'outils': "Unity 3D, C#, Python 3",
        #     'quick_description': "",
        #     'miniature': url_for('static', filename='img/miniature/runner_miniature.png'),
        #     'url': url_for('portfolio_bp.portfolio_runner'),
        #     'type': "Entreprise - Mission Freelance"
        # },
        {
            'name': "Plateforme Game",
            'outils': "Unity 3D, C#",
            'quick_description': "",
            'miniature': url_for('static', filename='general/img/miniature/plateforme_game_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_plateforme_game'),
            'type': "Personnel"
        },
        {
            'name': "Raytracer",
            'outils': "C++11, SDL2, CMake",
            'quick_description': "Un raytracer réalisé from scratch",
            'miniature': url_for('static', filename='general/img/miniature/raytracer_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_raytracer'),
            'type': "Universitaire"
        },
        # {
        #     'name': "Acronymos",
        #     'outils': "Python 3, HTML5, CSS3, JQuery",
        #     'quick_description': "Un générateur de texte à partir d'un acronyme",
        #     'miniature': url_for('static', filename='img/miniature/acronymos.png'),
        #     'url': url_for('portfolio_bp.portfolio_acronymos')
        # },
        {
            'name': "Anagramos",
            'outils': "Python 3, HTML5, CSS3, JQuery",
            'quick_description': "Permet de trouver tous les anagrames d'un mot dans la langue donné",
            'miniature': url_for('static', filename='general/img/miniature/anagramos_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_anagramos'),
            'type': "Personnel"
        },
        {
            'name': "String to leet",
            'outils': "Python 3, HTML5, CSS3, JQuery",
            'quick_description': "Permet de traduire une chaine de caractère en langage leet",
            'miniature': url_for('static', filename='general/img/miniature/string_to_leet_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_string_to_leet'),
            'type': "Personnel"
        },
        {
            'name': "2048",
            'outils': "Java 8, Swing",
            'quick_description': "Un 2048 réalisé en Java 8 avec spring",
            'miniature': url_for('static', filename='general/img/miniature/2048_miniature.png'),
            'url': url_for('portfolio_bp.portfolio_2048'),
            'type': "Universitaire"
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
    # Attention à l'odre dans la liste principal
    projects_m = projects()[0:3]
    # [
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3,Flask, Docker, HTML5, CSS3, Bootstrap4, Jinja2",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/miniature/sitePerso_miniature.png'),
    #         'url': url_for('portfolio_bp.portfolio_vahen_website')
    #     },
    #     {
    #         'name': "Webcrawler",
    #         'outils': "Python 3, Beautiful Soup 4",
    #         'quick_description': "Un webcrawler simple",
    #         'miniature': url_for('static', filename='img/miniature/webCrawler_miniature.png'),
    #         'url': url_for('portfolio_bp.portfolio_webcrawler')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/miniature/pacman_miniature.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    # ]
    return projects_m
