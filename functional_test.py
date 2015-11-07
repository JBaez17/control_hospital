from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Control Hospital', header_text)

        inputbox = self.browser.find_element_by_id('id_nombre')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Nombre')

        inputbox.send_keys('Juan')

        inputbox = self.browser.find_element_by_id('id_apellido')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Apellido')

        inputbox.send_keys('Baez')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_doctors_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.help_text == '1: Juan Baez' for row in rows),
            'No aparece ningun nombre en la tabla')

        self.fail('Completa el test!!!!')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
