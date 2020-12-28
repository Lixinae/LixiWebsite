import unittest

from application.apps.anagramos import anagramos_tests
from application.apps.string_to_leet import string_to_leet_tests
from application.apps.pendu import pendu_tests

def create_suite_api():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(anagramos_tests.TestAnagramosAPI)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(string_to_leet_tests.TestStringToLeetAPI)
    suite_pendu = unittest.TestLoader().loadTestsFromTestCase(pendu_tests.TestPenduAPI)

    # Todo Ajouter les autres test API une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos, suite_string_to_leet, suite_pendu])
    return alltests


if __name__ == '__main__':
    suite = create_suite_api()

    runner = unittest.TextTestRunner()
    runner.run(suite)
