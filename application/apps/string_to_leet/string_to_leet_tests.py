import unittest

from application import create_app
from application.apps.string_to_leet.string_to_leet_source import *
from application.configuration import TestingConfig


class TestStringToLeetUnitTest(unittest.TestCase):
    def test_dictionnary_setup(self):
        dic = setup_leet_dictionary()
        self.assertEqual(type(dic), dict)

    def test_pick_char_from_dict(self):
        dic = setup_leet_dictionary()
        trans_char = pick_char_from_dict("a", dic)
        self.assertEqual(type(trans_char), str)
        self.assertEqual(True, trans_char in dic["a"])

    def test_process_input(self):
        pass

    def test_strip_accents_no_accent(self):
        text = "NoAccent"
        stripped = strip_accents(text)
        self.assertEqual(stripped, text)

    def test_strip_accents_accent(self):
        text = "Accenté"
        stripped = strip_accents(text)
        self.assertEqual(stripped, "Accente")


class TestStringToLeetAPI(unittest.TestCase):
    def test_get_page(self):
        response = self.test_app.get(self.base_route)
        self.assertEqual(200, response.status_code)

    def test_get_data_ok(self):
        response = self.test_app.get(self.api_route + "translateToLeet", query_string={
            'phrase': 'hello'
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(dict, type(response.json))

    def test_get_data_wrong(self):
        response = self.test_app.get(self.api_route + "translateToLeet", query_string={
            'attr': 'value',
            'other': 'data'
        })
        self.assertEqual(400, response.status_code)

    def test_get_data_no_data(self):
        response = self.test_app.get(self.api_route + "translateToLeet")
        self.assertEqual(400, response.status_code)

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
        self.base_route = "/apps/string_to_leet/"
        self.api_route = self.base_route + "api/"
