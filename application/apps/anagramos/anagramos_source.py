from typing import List

from application.apps.common_data import apps_toolbox


def find_anagrammes(word: str, words: str) -> List[str]:
    """
    Take a word and finds all the anagrames of it
    :param word: Word for which we want to find the anagrames
    :param words: List of words where to find the anagrames
    :return: A list of all the anagrames of the given word
    """
    return [w for w in words if apps_toolbox.compare_letter_count(w, word)]
