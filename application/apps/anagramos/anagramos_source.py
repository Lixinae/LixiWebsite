from typing import List, Set


def compare_letter_count(origin: str, compared_to: str) -> bool:
    """
    Compares word_1 and word_2, returns True if they are anagrames
    :param origin: First word
    :param compared_to: Second word
    :return: True if origin and compared_to have the same length and the same amount of each letters
    """
    if type(origin) != str:
        return False
    origin = origin.lower().replace(" ", "")
    compared_to = compared_to.lower().replace(" ", "")
    if len(origin) != len(compared_to):
        return False
    return all([origin.count(letter) == compared_to.count(letter) for letter in origin])


def find_anagrammes(word: str, words: Set[str]) -> List[str]:
    """
    Take a word and finds all the anagrames of it
    :param word: Word for which we want to find the anagrames
    :param words: List of words where to find the anagrames
    :return: A list of all the anagrames of the given word
    """
    return [w for w in words if compare_letter_count(w, word)]
