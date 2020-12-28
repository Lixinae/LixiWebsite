import random
import unicodedata
from typing import Dict


def setup_leet_dictionary() -> Dict[str, str]:
    """
    Sets up the dictionary to translate a letter to its leet version
    """
    dictionary = {'a': ["/-\\", "/\\", "4", "@"],
                  'b': ["|3", "8", "|o", "13", "|}", "|:", "|8", "18", "6", "|B", "|8", "lo", "j3", "ß"],
                  'c': ["(", "<", "{", "[", "©", "¢"],
                  'd': ["|)", "o|", "|>", "<|", "|}", "|]"],
                  'e': ["3", "£", "₤", "€"],
                  'f': ["|=", "ph", "|#", "|"],
                  'g': ["(", "9", "6", "C-", "[+"],
                  'h': ["|-|", "]-[", "}-{", "(-)", ")-(", "#", "[-]", "{-}", "}{", "|=|", "[=]", "{=}", "/-/", ")-(", ":-:", "I+I"],
                  'i': ["l", "1", "|", "!", "]["],
                  'j': ["_|", "_/", "_7", "_)", "_]", "_}"],
                  'k': ["|<", "/<", "\<", "|{"],
                  'l': ["|_", "|", "1"],
                  'm': ["|\/|", "/\/\\", "|\'|\'|", "(\/)", "/\\\\", "/|\\", "/v\\"],
                  'n': ["|\|", "/\/", "|\\|", "/|/"],
                  'o': ["0", "()", "[]", "{}", "<>", "Ø", "oh"],
                  'p': ["|2", "|D", "|o", "|O", "|>", "|*", "|°", "/o", "[]D", "|7"],
                  'q': ["(,)", "kw", "O_", "9", "0"],
                  'r': ["|2", "|Z", "|?", "12", ".-", "|^", "l2", "Я"],
                  's': ["5", "$", "§"], 't': ["+", "\'][\'", "7"],
                  'u': ["|_|", "\_\\", "/_/", "\_/", "(_)", "[_]", "{_}"],
                  'v': ["|/", "\|", "\/", "/"],
                  'w': ["\/\/", "(/\)", "\^/", "|/\|", "\X/", "\\'", "'//", "VV", "\_|_/", "\\//\\//", "Ш", "2u", "\V/"],
                  'x': ["><", "}{", "%", "*", "><", ")(", "Ж"],
                  'y': ["`/", "'/", "j", "¥", "\|/", "Ч"],
                  'z': ["2", "(/)", "5", "7_", ">_"]}
    return dictionary


def pick_char_from_dict(char: str, dictionary: Dict[str, str]) -> str:
    """
    Picks a random format for the givin letter in the dictionary
    """
    return random.choice(dictionary[char])


def process_input(input_str: str, dictionary: Dict[str, str]) -> str:
    """
    Processes the input_str and produces an output string translated to leet
    """
    output_list = []
    for char in input_str:
        if char.isalpha():
            out_c = pick_char_from_dict(char.lower(), dictionary)
            output_list.append(out_c)
        else:
            output_list.append(char)
    return ''.join(output_list)


# A utiliser en dehors du module
def string_to_leet(input_str: str) -> str:
    """
    Sets up the dictionary and then returns the translated input string
    """
    dic = setup_leet_dictionary()
    # Todo -> Nettoyer la string d'input des accent
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    input_str = strip_accents(input_str)
    return process_input(input_str.lower(), dic)


def strip_accents(text: str) -> str:
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    # try:
    #     text = unicode(text, 'utf-8')
    # except (TypeError, NameError):  # unicode is a default on python 3
    #     pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
