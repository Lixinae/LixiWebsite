from typing import Set


def compare_letter_count_one_liner(word_1: str, word_2: str) -> bool:
    """
    Compares word_1 and word_2, returns True if they are anagrames
    :param word_1: First word
    :param word_2: Second word
    :return: True if word_1 and word_2 have the same length and the same amount of each letters
    """
    if len(word_1) != len(word_2):
        return False
    return all([word_1.count(letter) == word_2.count(letter) for letter in word_1])


def compare_letter_count(word_1: str, word_2: str) -> bool:
    """
    Compares word_1 and word_2, returns True if they are anagrames
    :param word_1: First word
    :param word_2: Second word
    :return: True if word_1 and word_2 have the same length and the same amount of each letters
    """
    output = []
    if len(word_1) != len(word_2):
        return False
    for letter in word_1:
        output.append(word_1.count(letter) == word_2.count(letter))
    return all(output)


def get_words_from_file(fname: str) -> Set[str]:
    """
    Parse a file and return a set of the words in it
    :param fname: File to parse
    :return: A set of words from the parsed file
    """
    with open(fname) as word_file:
        words = set(word_file.read().split())
    return words
