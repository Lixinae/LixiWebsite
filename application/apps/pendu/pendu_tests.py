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
        response = self.test_app.get(self.base_route)
        self.assertEqual(200, response.status_code)

    def test_parameters_get_page(self):
        response = self.test_app.get(self.api_route + "parameters")
        # Todo -> Check que le json renvoyé donne tous les paramètres
        # self.assertEqual()
        pass

    def test_parameters_get(self):
        response = self.test_app.get(self.api_route + "parameters",
                                     query_string={
                                         'param1': 'test1'
                                     })
        # Todo add parameters names to check
        # self.assertTrue((lambda : ))
        # self.assertEqual(response.json )
        pass

    def test_post_data_ok(self):
        pass

    def test_post_data_wrong(self):
        pass

    def test_post_data_no_data(self):
        pass

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
        self.base_route = "/apps/pendu/"
        self.api_route = self.base_route + "api/"
