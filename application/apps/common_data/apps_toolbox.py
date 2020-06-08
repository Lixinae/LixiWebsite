import os
from typing import Set

from flask import current_app


def compare_letter_count(origin: str, compared_to: str) -> bool:
    """
    Compares word_1 and word_2, returns True if they are anagrames
    :param origin: First word
    :param compared_to: Second word
    :return: True if origin and compared_to have the same length and the same amount of each letters
    """
    origin = origin.lower().replace(" ", "")
    compared_to = compared_to.lower().replace(" ", "")
    if len(origin) != len(compared_to):
        return False
    return all([origin.count(letter) == compared_to.count(letter) for letter in origin])


def get_words_from_file(fname: str, charset="utf-8") -> Set[str]:
    """
    Parse a file and return a set of the words in it
    :param charset: Charset of the given file
    :param fname: File to parse
    :return: A set of words from the parsed file
    """
    with current_app.open_resource(fname) as word_file:
        data = word_file.read().decode(charset)
        words = set(data.split())
    return words


# Folder where the list of words are stored
folder = "static/words_lists"


def get_english_words() -> Set[str]:
    fname = os.path.join(folder, "english_words.txt")
    """
    Returns the
    :param fname: File name
    :return: 
    """
    return get_words_from_file(fname)


def get_french_words() -> Set[str]:
    # fname = os.path.join(APP_STATIC, folder, "french_words.txt")
    fname = os.path.join(folder, "french_words.txt")
    """
    
    :param fname: 
    :return: 
    """
    return get_words_from_file(fname, charset="iso-8859-1")
