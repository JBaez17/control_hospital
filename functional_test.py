from selenium import webdriver
import unittest

class TestNuevoVisitante(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_ver_pagina_principal(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Control Hospital', self.browser.title)
        self.fail('Completa el test!!!!')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
