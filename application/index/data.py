from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def skills() -> List[Dict]:
    skills_list = [
        {
            'name': "Python",
            'img_url': url_for('static', filename='img/skills/python.png'),
            'img_alt': "Python 3 icon",
        },
        {
            'name': "Flask",
            'img_url': url_for('static', filename='img/skills/flask.png'),
            'img_alt': "Flask icon",
        },
        {
            'name': "Docker",
            'img_url': url_for('static', filename='img/skills/docker.png'),
            'img_alt': "Docker icon",
        },
        {
            'name': "VueJs",
            'img_url': url_for('static', filename='img/skills/vuejs.png'),
            'img_alt': "VueJs icon",
        },
        # {
        #     'name': "C++",
        #     'img_url': url_for('static', filename='img/skills/cpp.png'),
        #     'img_alt': "C++ icon",
        # },
        {
            'name': "Java",
            'img_url': url_for('static', filename='img/skills/java_2.png'),
            'img_alt': "Java icon",
        },
    ]
    return skills_list
