import unittest

from application import create_app, TestingConfig
from application.apps.anagramos.anagramos_source import find_anagrammes, compare_letter_count


class TestAnagramosUnitTest(unittest.TestCase):
    def test_find_anagrammes_ok(self):
        word = "étoile"
        words = {"étoile", "étiole", "soufflet", "bidule", "machin", "chose"}
        anagrams = find_anagrammes(word, words)
        self.assertEqual(list, type(anagrams))
        self.assertEqual(2, len(anagrams))

    def test_find_anagrammes_not_ok(self):
        word = "étoile"
        words = {"soufflet", "bidule", "machin", "chose"}
        anagrams = find_anagrammes(word, words)
        self.assertEqual(list, type(anagrams))
        self.assertEqual(0, len(anagrams))

    def test_find_anagrammes_numbers_in_list(self):
        word = "étoile"
        words = {1, "bidule", 3, "chose"}
        anagrams = find_anagrammes(word, words)
        self.assertEqual(list, type(anagrams))
        self.assertEqual(0, len(anagrams))

    def test_find_anagrammes_word_and_set_empty(self):
        word = ""
        words = {}
        anagrams = find_anagrammes(word, words)
        self.assertEqual(list, type(anagrams))
        self.assertEqual(0, len(anagrams))

    def test_compare_letter_count_ok_same_word(self):
        word_1 = "hello"
        word_2 = "hello"
        self.assertEqual(True, compare_letter_count(word_1, word_2))

    def test_compare_letter_count_ok_different_case(self):
        word_1 = "hello"
        word_2 = "HeLlO"
        self.assertEqual(True, compare_letter_count(word_1, word_2))

    def test_compare_letter_count_different_size(self):
        word_1 = "Paddle"
        word_2 = "Kid Paddle"
        self.assertEqual(False, compare_letter_count(word_1, word_2))

    def test_compare_letter_count_wrong_type(self):
        word_1 = 10
        word_2 = False
        self.assertEqual(False, compare_letter_count(word_1, word_2))


class TestAnagramosAPI(unittest.TestCase):
    def test_get_data(self):
        response = self.test_app.get("/apps/anagramos/")
        self.assertEqual(200, response.status_code)

    def test_post_data_ok(self):
        response = self.test_app.post("/apps/anagramos/api/askForAnagrams", json={
            "word": "étoile",
            "language_select": "French"
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(dict, type(response.json))

    def test_post_data_wrong(self):
        response = self.test_app.post("/apps/anagramos/api/askForAnagrams", json={
            'attr': 'value', 'other': 'data'
        })
        self.assertEqual(400, response.status_code)

    def test_post_data_no_data(self):
        response = self.test_app.post("/apps/anagramos/api/askForAnagrams")
        self.assertEqual(400, response.status_code)

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
