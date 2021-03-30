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
    ]
    return skills


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "Python",
            'img_url': url_for('static', filename='general/img/skills/python.png'),
            'img_alt': "Python 3 icon",
        },
    ]
    return skills
