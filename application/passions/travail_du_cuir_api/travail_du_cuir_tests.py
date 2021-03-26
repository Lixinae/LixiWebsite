import unittest

from application import create_app
from application.configuration import TestingConfig


class TestTravailDuCuirUnitTest(unittest.TestCase):
    def test_(self):
        pass


class TestTravailDuCuirAPI(unittest.TestCase):
    def test_get_page(self):
        pass

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
        self.base_route = "/passions/travail_du_cuir/"
        self.api_route = self.base_route + "api/"
