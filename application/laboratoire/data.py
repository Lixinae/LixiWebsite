from typing import List, Dict

from flask import url_for


def laboratoire_list() -> List[Dict]:
    laboratoire_l = [
        {
            'name': "Website Stats",
            'quick_description': "Un module pour voir les statistique de visites du site",
            'miniature': url_for('static', filename='img/miniature/website_stats.png'),
            'url': url_for('website_stats_bp.website_stats')
        },
    ]
    return laboratoire_l
