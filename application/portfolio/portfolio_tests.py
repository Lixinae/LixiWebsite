import unittest

from application import create_app, TestingConfig


class PortfolioTestApi(unittest.TestCase):
    def test_portfolio_base_route(self):
        response = self.test_app.get("/portfolio/")
        self.assertEqual(200, response.status_code)

    def test_portfolio_vahen_website(self):
        response = self.test_app.get("/portfolio/vahen_website")
        self.assertEqual(200, response.status_code)

    def test_portfolio_pacman3d(self):
        response = self.test_app.get("/portfolio/pacman3d")
        self.assertEqual(200, response.status_code)

    def test_portfolio_webcrawler(self):
        response = self.test_app.get("/portfolio/webcrawler")
        self.assertEqual(200, response.status_code)

    def test_portfolio_raytracer(self):
        response = self.test_app.get("/portfolio/raytracer")
        self.assertEqual(200, response.status_code)

    def test_portfolio_plateforme_game(self):
        response = self.test_app.get("/portfolio/plateforme_game")
        self.assertEqual(200, response.status_code)

    def test_portfolio_runner(self):
        response = self.test_app.get("/portfolio/runner")
        self.assertEqual(200, response.status_code)

    # def test_portfolio_acronymos(self):
    #     response = self.test_app.get("/portfolio/acronymos")
    #     self.assertEqual(200, response.status_code)

    def test_portfolio_anagramos(self):
        response = self.test_app.get("/portfolio/anagramos")
        self.assertEqual(200, response.status_code)

    def test_portfolio_string_to_leet(self):
        response = self.test_app.get("/portfolio/string_to_leet")
        self.assertEqual(200, response.status_code)

    def test_portfolio_2048(self):
        response = self.test_app.get("/portfolio/2048")
        self.assertEqual(200, response.status_code)

    def setUp(self):
        self.test_app = create_app(TestingConfig).test_client()

