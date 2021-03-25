import unittest

from application import create_app, TestingConfig


# Todo -> Réaliser les test unitaires une fois le code bon
class TestPenduUnitTest(unittest.TestCase):
    def test_compare_letter_count_ok(self):
        pass

    def test_compare_letter_count_different_size(self):
        pass

    def test_compare_letter_count_wrong_type(self):
        pass


class TestPenduAPI(unittest.TestCase):
    def test_get_data(self):
        response = self.test_app.get("/apps/pendu/")
        self.assertEqual(200, response.status_code)

    def test_post_data_ok(self):
        pass

    def test_post_data_wrong(self):
        pass

    def test_post_data_no_data(self):
        pass

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
