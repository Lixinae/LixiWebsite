from typing import List, Dict

from flask import url_for


# from application import models


# Permet de query la liste de tous les projets
def skills_front() -> List[Dict]:
    skills = [
        {
        },
    ]
    return skills


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "C++",
            'img_url': url_for('static', filename='img/skills/cpp.png'),
            'img_alt': "Python 3 icon",
        },
        {
            'name': "CMake",
            'img_url': url_for('static', filename='img/skills/cmake.png'),
            'img_alt': "BeautifulSoup icon",
        },
        {
            'name': "SDL2",
            'img_url': url_for('static', filename='img/skills/sdl.png'),
            'img_alt': "SDL2 icon",
        },

    ]
    return skills
