import random
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
    return process_input(input_str, dic)

# if __name__ == '__main__':
#     allPhrasesSaid = []
#     dico = setup_leet_dictionary()
#     while True:
#         inputString = input("Enter a phrase to translate to leet\n")
#         outPutString = process_input(inputString, dico)
#         allPhrasesSaid.append(outPutString)
#         print(outPutString)
#         if inputString == "exit":
#             print("Leaving program")
#             break
#
#     print("Here is everything said since the launch")
#     for p in allPhrasesSaid:
#         print(p)