import unittest

from application.apps.stringToLeet.stringToLeet_source import *


class TestStringToLeetSource(unittest.TestCase):
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
        pass

    def test_post_data_ok(self):
        pass

    def test_post_data_wrong(self):
        pass


if __name__ == '__main__':
    unittest.main()
