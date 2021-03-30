from typing import List, Dict

from flask import url_for


def skills_front() -> List[Dict]:
    skills = [
    ]
    return skills


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "C++",
            'img_url': url_for('static', filename='general/img/skills/cpp.png'),
            'img_alt': "Python 3 icon",
        },
        {
            'name': "CMake",
            'img_url': url_for('static', filename='general/img/skills/cmake.png'),
            'img_alt': "BeautifulSoup icon",
        },
        {
            'name': "SDL2",
            'img_url': url_for('static', filename='general/img/skills/sdl.png'),
            'img_alt': "SDL2 icon",
        },

    ]
    return skills


def screenshots() -> List[Dict]:
    screenshots_list = [
        {
            'name': "AA_1",
            'img_url': url_for('static', filename='general/img/projects/screenshots/raytracer/AA1.png'),
            'img_alt': "AA1 screenshot",
        },
        {
            'name': "AA_4",
            'img_url': url_for('static', filename='general/img/projects/screenshots/raytracer/AA4.png'),
            'img_alt': "AA_4 screenshot",
        },
        {
            'name': "AA_8",
            'img_url': url_for('static', filename='general/img/projects/screenshots/raytracer/AA8.png'),
            'img_alt': "AA_8 screenshot",
        },
        {
            'name': "AA_16",
            'img_url': url_for('static', filename='general/img/projects/screenshots/raytracer/AA16.png'),
            'img_alt': "AA_16 screenshot",
        },
        {
            'name': "Objets aleatoires",
            'img_url': url_for('static',
                               filename='general/img/projects/screenshots/raytracer/Generation_Objets_aleatoire.png'),
            'img_alt': "AA1 screenshot",
        },
        {
            'name': "Transparence 50%",
            'img_url': url_for('static',
                               filename='general/img/projects/screenshots/raytracer/Transparence_50%_sans_ombre.png'),
            'img_alt': "Transparence 50% screenshot",
        },
    ]
    return screenshots_list
