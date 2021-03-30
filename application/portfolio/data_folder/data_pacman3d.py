from typing import List, Dict

from flask import url_for


def skills_front() -> List[Dict]:
    return []


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "C++ 11",
            'img_url': url_for('static', filename='general/img/skills/cpp.png'),
            'img_alt': "C++ icon",
        },
        {
            'name': "CMake",
            'img_url': url_for('static', filename='general/img/skills/cmake.png'),
            'img_alt': "BeautifulSoup icon",
        },
        {
            'name': "SDL1.2",
            'img_url': url_for('static', filename='general/img/skills/sdl.png'),
            'img_alt': "SDL2 icon",
        },
        {
            'name': "OpenGL 3",
            'img_url': url_for('static', filename='general/img/skills/openGL.png'),
            'img_alt': "OpenGL icon",
        },
        {
            'name': "Python",
            'img_url': url_for('static', filename='general/img/skills/python.png'),
            'img_alt': "Python 3 icon",
        },

    ]
    return skills


def screenshots() -> List[Dict]:
    screenshots_list = [
        {
            'name': "Camera de base",
            'img_url': url_for('static', filename='general/img/projects/screenshots/pacman3d/camera_base.png'),
            'img_alt': "Camera de base screenshot",
        },
        {
            'name': "Camera fps",
            'img_url': url_for('static', filename='general/img/projects/screenshots/pacman3d/camera_fps.png'),
            'img_alt': "Camera fps screenshot",
        },
        {
            'name': "Camera Oblique 1",
            'img_url': url_for('static', filename='general/img/projects/screenshots/pacman3d/camera_oblique_1.png'),
            'img_alt': "Camera Oblique 1 screenshot",
        },
        {
            'name': "Camera Oblique 2",
            'img_url': url_for('static', filename='general/img/projects/screenshots/pacman3d/camera_oblique_2.png'),
            'img_alt': "Camera Oblique 2 screenshot",
        },
    ]
    return screenshots_list
