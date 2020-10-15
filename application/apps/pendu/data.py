from typing import List
import random

numb_attempts = 8

# To
words = ["test", "bidule", "ordinateur"]


def pick_random_word_from_list(word_list: List):
    word = random.choice(word_list)
    return [(x, False) for x in word]
