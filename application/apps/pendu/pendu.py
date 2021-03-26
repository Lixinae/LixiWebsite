from typing import List

from application.apps.pendu.data import numb_attempts, pick_random_word_from_list, words


class Pendu:

    def __init__(self):
        self.word_to_find = pick_random_word_from_list(words)
        self.number_of_attempts = 10
        self.win = False
        self.current_discovered_word = []
        self.tried_letters = []

    def initialize_game(self):
        pass

    def update_parameters(self, number_of_attempts):
        pass

    def word_found_letters(self, word: List) -> str:
        out_word_str = ""
        for tup in word:
            if tup[1]:
                out_word_str += tup[0]
            else:
                out_word_str += "_"
        return out_word_str

    def mark_letters_in_word(self, letter: str, word_: List) -> List:
        # Todo -> Refaire pour correspondre à l'objet
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

    def check_if_letter_in_word(self, letter: str) -> bool:
        return letter in self.word_to_find

    def check_if_lost(self) -> bool:
        return self.number_of_attempts <= 0

    def decrease_attempts(self) -> None:
        if self.number_of_attempts > 0:
            self.number_of_attempts -= 1
        else:
            self.number_of_attempts = 0

    def check_win_condition(self):
        pass


if __name__ == '__main__':
    win = False
    # Pick number of attempts
    # Game loop
    # Pick random word
    pendu = Pendu()
    word = pick_random_word_from_list(words)
    word_marked = word
    while numb_attempts > 0 and not win:
        # Display found letters
        print(pendu.word_found_letters(word_marked))
        # Ask player to guess letter
        letter = input("Entrez une lettre:")
        if len(letter) != 1 or letter.isdigit():
            print("Entrez une seule lettre")
            continue
        if letter in [x[0] for x in word_marked]:
            # If letter correct -> Mark letters as seen from word
            word_marked = pendu.mark_letters_in_word(letter, word_marked)
        else:
            # If incorrect -> decrement
            numb_attempts -= 1

        # Display number of attemps left
        print("Vous avez encore " + str(numb_attempts) + " essais")

        if all([x[1] for x in word_marked]):
            win = True
            print(pendu.word_found_letters(word_marked))
    if win:
        print("You win")
    else:
        print("You loose")
