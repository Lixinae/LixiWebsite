import unittest

from application import TestingConfig, create_app, db
from application.apps.data import app_list


class DbUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_something(self):
        pass
        self.assertEqual(True, False)
