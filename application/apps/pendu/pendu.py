from typing import List

from application.apps.pendu.data import numb_attempts, pick_random_word_from_list, words


def word_found_letters(word_: List) -> str:
    out_word_str = ""
    for tup in word_:
        if tup[1]:
            out_word_str += tup[0]
        else:
            out_word_str += "_"
    return out_word_str


def mark_letters_in_word(letter, word_: List) -> List:
    word_marked = []
    for tup in word_:
        if not tup[1]:
            if tup[0] == letter:
                word_marked.append((tup[0], True))
            else:
                word_marked.append(tup)
        else:
            word_marked.append(tup)
    return word_marked


# if __name__ == '__main__':
#     win = False
#     # Pick number of attempts
#     # Game loop
#     # Pick random word
#     word = pick_random_word_from_list(words)
#     while numb_attempts > 0 and not win:
#         # Display found letters
#         print(word_found_letters(word))
#         # Ask player to guess letter
#         letter = input("Entrez une lettre:")
#         if len(letter) != 1 or letter.isdigit():
#             print("Entrez une seule lettre")
#             continue
#         if letter in [x[0] for x in word]:
#             # If letter correct -> Mark letters as seen from word
#             word = mark_letters_in_word(letter, word)
#         else:
#             # If incorrect -> decrement
#             numb_attempts -= 1
#
#         # Display number of attemps left
#         print("Vous avez encore " + str(numb_attempts) + " essais")
#
#         if all([x[1] for x in word]):
#             win = True
#             print(word_found_letters(word))
#     if win:
#         print("You win")
#     else :
#         print("You loose")
