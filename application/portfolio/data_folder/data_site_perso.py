from typing import List, Dict

from flask import url_for


# from application import models


# Permet de query la liste de tous les projets
def skills_front() -> List[Dict]:
    skills = [
        {
            'name': "HTML5",
            'img_url': url_for('static', filename='general/img/skills/html5.png'),
            'img_alt': "HTML5 icon",
        },
        {
            'name': "CSS3",
            'img_url': url_for('static', filename='general/img/skills/css3.png'),
            'img_alt': "CSS3 icon",
        },
        {
            'name': "VueJs",
            'img_url': url_for('static', filename='general/img/skills/vuejs.png'),
            'img_alt': "VueJs icon",
        },
        {
            'name': "JQuery",
            'img_url': url_for('static', filename='general/img/skills/jquery.png'),
            'img_alt': "JQuery icon",
        },
        {
            'name': "Bootstrap 4",
            'img_url': url_for('static', filename='general/img/skills/bootstrap4.png'),
            'img_alt': "Bootstrap icon",
        },
        {
            'name': "Jinja 2",
            'img_url': url_for('static', filename='general/img/skills/jinja2.png'),
            'img_alt': "Jinja 2 icon",
        },

    ]
    return skills


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "Python",
            'img_url': url_for('static', filename='general/img/skills/python.png'),
            'img_alt': "Python 3 icon",
        },
        {
            'name': "Flask",
            'img_url': url_for('static', filename='general/img/skills/flask.png'),
            'img_alt': "Python 3 icon",
        },
        {
            'name': "Docker",
            'img_url': url_for('static', filename='general/img/skills/docker.png'),
            'img_alt': "Docker icon",
        },

    ]
    return skills
