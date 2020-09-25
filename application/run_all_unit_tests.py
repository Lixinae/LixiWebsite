import unittest

from application.apps.anagramos import anagramos_tests
from application.apps.stringToLeet import stringToLeet_tests


def create_suite_unit_test():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(anagramos_tests.TestAnagramosUnitTest)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(stringToLeet_tests.TestStringToLeetUnitTest)
    # Todo Ajouter les autres test unit test une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos, suite_string_to_leet])
    return alltests


if __name__ == '__main__':
    suite = create_suite_unit_test()

    runner = unittest.TextTestRunner()
    runner.run(suite)
