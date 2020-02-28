from typing import List, Dict

from flask import url_for


# Permet de query la liste de tous les projets
def skills_passion() -> List[Dict]:
    # Todo -> Eventuellement faire une BDD ici pour séparer le code du contenu
    skill_passion_list = [
        {
            'name': "GN",
            'quick_description': "Gn : Jeux de role grandeur nature",
            'miniature': url_for('static', filename='img/miniature/gn_miniature.png'),
            'url': url_for('skills_passion_bp.skills_passion_gn')
        },
        {
            'name': "Travail du cuir",
            'quick_description': "Mes différentes réalisation en travail du cuir",
            'miniature': url_for('static', filename='img/miniature/tdc_miniature.png'),
            'url': url_for('skills_passion_bp.skills_passion_travail_du_cuir')
        },
        {
            'name': "Serveur personnel",
            'quick_description': "Mon serveur personnel monté sur une ancienne machine",
            'miniature': url_for('static', filename='img/miniature/serveur_miniature.png'),
            'url': url_for('skills_passion_bp.skills_passion_serveur_multimedia')
        },
        {
            'name': "Jeux de rôle",
            'quick_description': "Les différents jeux de rôle auxquels j'ai joué, mes différents personnages dans ces mondes",
            'miniature': url_for('static', filename='img/miniature/jdr_miniature_250.png'),
            'url': url_for('skills_passion_bp.skills_passion_jeux_de_role')
        },
        {
            'name': "Jeux de societe",
            'quick_description': "Les differents jeux de société auxquels j'aime jouer",
            'miniature': url_for('static', filename='img/miniature/jeux_societe_miniature.png'),
            'url': url_for('skills_passion_bp.skills_passion_jeux_de_societe')
        }
    ]

    return skill_passion_list
