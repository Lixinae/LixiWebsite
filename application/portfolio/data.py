from typing import List, Dict

from flask import url_for
from application import models


# Permet de query la liste de tous les projets
def projects() -> List[Dict]:
    # Todo -> Faire un Select * from Project sur la BDD ici
    # projects_query = [
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/miniature/pacman_miniature.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3,Flask, SqlLite, Docker, HTML5, CSS3, Bootstrap4, Jinja2",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/miniature/sitePerso_miniature.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    #     {
    #         'name': "Pacman3D",
    #         'outils': "C++11, OpenGL3+",
    #         'quick_description': " Un pacman en 3D",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_pacman3d')
    #     },
    #     {
    #         'name': "Vahen website",
    #         'outils': "Python 3",
    #         'quick_description': "Mon site personnel fait en Python 3 / Flask",
    #         'miniature': url_for('static', filename='img/skills/cpp.png'),
    #         'url': url_for('portfolio_bp.portfolio_site_perso')
    #     },
    # ]

    projects_query = models.Project.query.all()
    output_list_project = []
    for project in projects_query:
        project_dict = project.to_dict()
        output_list_project.append(project_dict)
    return output_list_project


# Permet de query un projet en particulier
# Si l'on ne passe pas de projet -> Renvoie un dictionnaire vide
def project_specific(project_name="") -> Dict:
    if project_name == "":
        return {}

    project = models.Project.query.get_or_404(project_name)
    return project.to_dict()
