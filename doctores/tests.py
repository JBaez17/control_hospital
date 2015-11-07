from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from doctores.views import home_page


class TestPaginaPrincipal(TestCase):

    def test_url_principal_retorna_a_vista_pagina_principal(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_principal_retorna_el_html_correcto(self):
        request = HttpRequest()
        response = home_page(request)
        """self.assertTrue(response.content.startswith("<html>"))
        self.assertIn(b'<title>Control Hospital</title>', response.content)
        self.assertTrue(response.content.endswith("</html>"))"""
        expected_html = render_to_string('home.html')
        # se usa decode() para convertir la response.content
        # de bytes a una cadena unicode
        self.assertEqual(response.content.decode(), expected_html)
