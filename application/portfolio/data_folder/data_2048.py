from typing import List, Dict

from flask import url_for


# from application import models


# Permet de query la liste de tous les projets
def skills_front() -> List[Dict]:
    skills = [
    ]
    return skills


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "Java",
            'img_url': url_for('static', filename='img/skills/java_2.png'),
            'img_alt': "Java icon",
        },
    ]
    return skills


def screenshots() -> List[Dict]:
    screenshots_list = [
        {
            'name': "2048",
            'img_url': url_for('static', filename='img/projects/screenshots/2048/2048.png'),
            'img_alt': "2048 screenshot",
        },
    ]
    return screenshots_list
