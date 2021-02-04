import unittest

from application.apps.anagramos.anagramos_tests import TestAnagramosAPI
from application.apps.string_to_leet.string_to_leet_tests import TestStringToLeetAPI
from application.apps.pendu.pendu_tests import TestPenduAPI

def create_suite_api():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(TestAnagramosAPI)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(TestStringToLeetAPI)
    suite_pendu = unittest.TestLoader().loadTestsFromTestCase(TestPenduAPI)

    # Todo Ajouter les autres test API une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos, suite_string_to_leet, suite_pendu])
    return alltests


if __name__ == '__main__':
    suite = create_suite_api()

    runner = unittest.TextTestRunner()
    runner.run(suite)
