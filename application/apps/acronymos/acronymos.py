import random

# Todo -> Terminer les corrections
from typing import Set, List


def create_acronyme(string: str) -> str:
    return ''.join([x[0] for x in string.split(" ")])


def pick_random_word_by_letter(letter: str, words: Set[str]) -> str:
    words_starting_by = find_list_words_starting_by(letter, words)
    return words_starting_by[random.randint(len(words_starting_by))]


def find_list_words_starting_by(letter: str, words: Set[str]) -> List[str]:
    return [x for x in words if x.upper().startswith(letter.upper())]


def unroll_acronyme(acronyme: str, words: Set[str]) -> str:
    return ' '.join([pick_random_word_by_letter(x, words) for x in acronyme])
