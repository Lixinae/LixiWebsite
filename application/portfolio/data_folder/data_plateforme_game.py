from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def skills_front() -> List[Dict]:
    return []


def skills_back() -> List[Dict]:
    skills = [
        {
            'name': "Unity",
            'img_url': url_for('static', filename='img/skills/unity_small.png'),
            'img_alt': "Unity icon",
        },
        {
            'name': "C#",
            'img_url': url_for('static', filename='img/skills/c#.png'),
            'img_alt': "C# icon",
        },

    ]
    return skills
