import unittest

from application import create_app
from application.apps.stringToLeet.stringToLeet_source import *
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
    def test_get_data(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.get("/apps/string_to_leet/")
        self.assertEqual(200, response.status_code)

    def test_post_data_ok(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/string_to_leet/", json={
            'phrase': 'hello'
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(dict, type(response.json))

    def test_post_data_wrong(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/string_to_leet/", json={
            'attr': 'value', 'other': 'data'
        })
        self.assertEqual(400, response.status_code)

    def test_post_data_no_data(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/string_to_leet/")
        self.assertEqual(400, response.status_code)
