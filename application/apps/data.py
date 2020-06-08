from typing import List, Dict

from flask import url_for


def app_list() -> List[Dict]:
    apps_list = [
        {
            'name': "Webcrawler",
            'quick_description': "Un crawler pour parser / scrap du contenu en ligne",
            'miniature': url_for('static', filename='img/miniature/webcrawler_miniature.png'),
            'url': url_for('webcrawler_bp.webcrawler')
        },
        # {
        #     'name': "Acronymos",
        #     'quick_description': "Un générateur de texte à partir d'un acronyme",
        #     'miniature': url_for('static', filename='img/miniature/acronymos_miniature.png'),
        #     'url': url_for('acronymos_bp.acronymos')
        # },
        {
            'name': "Anagramos",
            'quick_description': "Permet de trouver tous les anagrames d'un mot dans la langue donné",
            'miniature': url_for('static', filename='img/miniature/anagramos_miniature.png'),
            'url': url_for('anagramos_bp.anagramos_page')
        },
        {
            'name': "String to leet",
            'quick_description': "Permet de traduire une chaine de caractère en langage leet",
            'miniature': url_for('static', filename='img/miniature/string_to_leet_miniature.png '),
            'url': url_for('string_to_leet_bp.string_to_leet')
        },
    ]
    return apps_list
