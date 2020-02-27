from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def projects() -> List[Dict]:
    # Todo -> Faire un Select * from Project sur la BDD ici
    projects_m = [
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/miniature/pacman_miniature.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
        {
            'name': "Pacman3D",
            'outils': "C++11, OpenGL3+",
            'quick_description': " Un pacman en 3D",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_pacman3d')
        },
        {
            'name': "Vahen website",
            'outils': "Python 3",
            'quick_description': "Mon site personnel fait en Python 3 / Flask",
            'miniature': url_for('static', filename='img/skills/cpp.png'),
            'url': url_for('portfolio_site_perso')
        },
    ]
    return projects_m


# Permet de query un projet en particulier
# Si l'on ne passe pas de projet -> Renvoie un dictionnaire vide
def project_specific(project_name="") -> Dict:
    if project_name == "":
        return {}
    # Todo -> Faire un Select * from Project where title=projectName
    project = {

    }
    return project
