from typing import List
import random

numb_attempts = 8

# Todo -> Avoir une vrai liste (Appel en BDD par exemple ou autre)
words = ["test", "bidule", "ordinateur"]


def pick_random_word_from_list(word_list: List) -> List[tuple[str, bool]]:
    word = random.choice(word_list)
    return [(x, False) for x in word]
