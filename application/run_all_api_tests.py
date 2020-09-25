import unittest

from application.apps.anagramos import anagramos_tests
from application.apps.stringToLeet import stringToLeet_tests


def create_suite_api():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(anagramos_tests.TestAnagramosAPI)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(stringToLeet_tests.TestStringToLeetAPI)
    # Todo Ajouter les autres test API une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos, suite_string_to_leet])
    return alltests


if __name__ == '__main__':
    suite = create_suite_api()

    runner = unittest.TextTestRunner()
    runner.run(suite)
