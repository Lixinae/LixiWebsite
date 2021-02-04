import unittest

from application.apps.anagramos.anagramos_tests import TestAnagramosUnitTest
from application.apps.string_to_leet.string_to_leet_tests import TestStringToLeetUnitTest
from application.apps.pendu.pendu_tests import TestPenduUnitTest


def create_suite_unit_test():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(TestAnagramosUnitTest)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(TestStringToLeetUnitTest)
    suite_pendu = unittest.TestLoader().loadTestsFromTestCase(TestPenduUnitTest)
    # Todo Ajouter les autres test unit test une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos, suite_string_to_leet, suite_pendu])
    return alltests


if __name__ == '__main__':
    suite = create_suite_unit_test()

    runner = unittest.TextTestRunner()
    runner.run(suite)
