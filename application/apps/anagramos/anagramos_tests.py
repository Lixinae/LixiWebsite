import unittest

from application import create_app, TestingConfig


class TestAnagramosUnitTest(unittest.TestCase):
    def test_find_anagrammes(self):
        # Todo
        pass


class TestAnagramosAPI(unittest.TestCase):
    def test_get_data(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.get("/apps/anagramos/")
        self.assertEqual(200, response.status_code)

    def test_post_data_ok(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/anagramos/", json={

        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(dict, type(response.json))

    def test_post_data_wrong(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/anagramos/", json={
            'attr': 'value', 'other': 'data'
        })
        self.assertEqual(400, response.status_code)

    def test_post_data_no_data(self):
        test_app = create_app(TestingConfig).test_client()
        response = test_app.post("/apps/anagramos/")
        self.assertEqual(400, response.status_code)
