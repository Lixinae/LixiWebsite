from typing import List, Dict
from application.apps.app_model import Apps


def app_list():
    applications = Apps.query.all()
    return applications

# def app_list() -> List[Dict]:
#     apps_list = [
#         {
#             'name': "Webcrawler",
#             'quick_description': "Un crawler pour parser / scrap du contenu en ligne",
#             'miniature_path': 'img/miniature/webcrawler_miniature.png',
#             'url': 'webcrawler_bp.webcrawler_page'
#         },
#         # {
#         #     'name': "Acronymos",
#         #     'quick_description': "Un générateur de texte à partir d'un acronyme",
#         #     'miniature': url_for('static', filename='img/miniature/acronymos_miniature.png'),
#         #     'url': url_for('acronymos_bp.acronymos')
#         # },
#         {
#             'name': "Anagramos",
#             'quick_description': "Permet de trouver tous les anagrames d'un mot dans la langue donné",
#             'miniature_path': 'img/miniature/anagramos_miniature.png',
#             'url': 'anagramos_bp.anagramos_page'
#         },
#         {
#             'name': "String to leet",
#             'quick_description': "Permet de traduire une chaine de caractère en langage leet",
#             'miniature_path': 'img/miniature/string_to_leet_miniature.png',
#             'url': 'string_to_leet_bp.string_to_leet_page'
#         },
#     ]
#     return apps_list
