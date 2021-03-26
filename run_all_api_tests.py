import sys
import unittest

from application.apps.anagramos.anagramos_tests import TestAnagramosAPI
from application.apps.string_to_leet.string_to_leet_tests import TestStringToLeetAPI
from application.apps.pendu.pendu_tests import TestPenduAPI
from application.passions.travail_du_cuir_api.travail_du_cuir_tests import TestTravailDuCuirAPI
from application.portfolio.portfolio_tests import PortfolioTestApi


def create_suite_api():
    suite_anagramos = unittest.TestLoader().loadTestsFromTestCase(TestAnagramosAPI)
    suite_string_to_leet = unittest.TestLoader().loadTestsFromTestCase(TestStringToLeetAPI)
    suite_pendu = unittest.TestLoader().loadTestsFromTestCase(TestPenduAPI)
    suite_portfolio = unittest.TestLoader().loadTestsFromTestCase(PortfolioTestApi)
    suite_tdc = unittest.TestLoader().loadTestsFromTestCase(TestTravailDuCuirAPI)

    # Todo Ajouter les autres test API une fois qu'ils seront codé
    alltests = unittest.TestSuite([suite_anagramos,
                                   suite_string_to_leet,
                                   suite_pendu,
                                   suite_portfolio,
                                   suite_tdc])
    return alltests


if __name__ == '__main__':
    suite = create_suite_api()

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
