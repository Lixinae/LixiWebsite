from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def passions() -> List[Dict]:
    passion_list = [
        {
            'name': "GN",
            'miniature': url_for('static', filename='img/miniature/gn_miniature.png'),
            'url': url_for('passions_bp.passions_gn')
        },
        {
            'name': "Travail du cuir",
            'miniature': url_for('static', filename='img/miniature/tdc_miniature.png'),
            'url': url_for('passions_bp.passions_travail_du_cuir')
        },
        {
            'name': "Jeux de rôle",
            'miniature': url_for('static', filename='img/miniature/jdr_miniature_250_250.png'),
            'url': url_for('passions_bp.passions_jeux_de_role')
        },
        {
            'name': "Jeux de societe",
            'miniature': url_for('static', filename='img/miniature/jeux_societe_miniature.png'),
            'url': url_for('passions_bp.passions_jeux_de_societe')
        }
    ]
    return passion_list


def passions_short() -> List[Dict]:
    passion_list = [
        {
            'name': "GN",
            'miniature': url_for('static', filename='img/miniature/gn_miniature.png'),
            'url': url_for('passions_bp.passions_gn')
        },
        {
            'name': "Travail du cuir",
            'miniature': url_for('static', filename='img/miniature/tdc_miniature.png'),
            'url': url_for('passions_bp.passions_travail_du_cuir')
        },
    ]

    return passion_list
