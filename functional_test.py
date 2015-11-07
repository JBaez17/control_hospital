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
        self.fail('Completa el test!!!!')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Nombre')

        inputbox.send_keys('Juan')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Nombre')

        inputbox.send_keys('Baez')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find.elements_by_tag_name('tr')
        self.assertTrue(
            any(row.help_text== '1: Juan Baez' for row in rows))

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
