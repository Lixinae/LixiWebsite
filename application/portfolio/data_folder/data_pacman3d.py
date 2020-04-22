from typing import List, Dict

from flask import url_for


# from application import models


# Permet de query la liste de tous les projets
def skills_front() -> List[Dict]:
    return []


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "C++ 11",
            'img_url': url_for('static', filename='img/skills/cpp.png'),
            'img_alt': "C++ icon",
        },
        {
            'name': "CMake",
            'img_url': url_for('static', filename='img/skills/cmake.png'),
            'img_alt': "BeautifulSoup icon",
        },
        {
            'name': "SDL1.2",
            'img_url': url_for('static', filename='img/skills/sdl.png'),
            'img_alt': "SDL2 icon",
        },
        {
            'name': "OpenGL 3",
            'img_url': url_for('static', filename='img/skills/openGL.png'),
            'img_alt': "OpenGL icon",
        },
        {
            'name': "Python",
            'img_url': url_for('static', filename='img/skills/python.png'),
            'img_alt': "Python 3 icon",
        },

    ]
    return skills
