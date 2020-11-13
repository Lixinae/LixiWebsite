import unittest

from application import TestingConfig, create_app,db


class DbUnitTest(unittest.TestCase):
    def setUp(self):

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_something(self):
        test_app = create_app(TestingConfig).test_client()

        self.assertEqual(True, False)
