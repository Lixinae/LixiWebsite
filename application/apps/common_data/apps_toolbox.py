import os
from typing import Set



def get_words_from_file(fname: str, charset="utf-8") -> Set[str]:
    """
    Parse a file and return a set of the words in it
    :param charset: Charset of the given file
    :param fname: File to parse
    :return: A set of words from the parsed file
    """
    from flask import current_app
    with current_app.open_resource(fname) as word_file:
        data = word_file.read().decode(charset)
        words = set(data.split())
    return words


def get_english_words() -> Set[str]:
    # Folder where the list of words are stored
    folder = "static/words_lists"
    fname = os.path.join(folder, "english_words.txt")
    """
    Renvoie la liste des mots anglais
    :param fname: Le fichier contenant les mots anglais
    :return: La liste des mots anglais
    """
    return get_words_from_file(fname)


def get_french_words() -> Set[str]:
    # Folder where the list of words are stored
    folder = "static/words_lists"
    # fname = os.path.join(APP_STATIC, folder, "french_words.txt")
    fname = os.path.join(folder, "french_words.txt")
    """
    Renvoie la liste des mots français
    :param fname: Le fichier contenant les mots français
    :return: La liste des mots anglais
    """
    return get_words_from_file(fname, charset="iso-8859-1")
