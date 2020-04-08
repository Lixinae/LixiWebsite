from typing import List, Dict

from flask import url_for


def app_list() -> List[Dict]:
    apps_list = [
        {
            'name': "Webcrawler",
            'quick_description': "Un crawler pour parser / scrap du contenu en ligne",
            'miniature': url_for('static', filename='img/miniature/webcrawler.png'),
            'url': url_for('webcrawler_bp.webcrawler')
        },
    ]
    return apps_list
