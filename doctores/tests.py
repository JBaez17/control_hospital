from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from doctores.views import home_page


class TestPaginaPrincipal(TestCase):

    def test_url_principal_retorna_a_vista_pagina_principal(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_pagina_principal_retorna_el_html_correcto(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith("<html>"))
        self.assertIn(b'<title>Control Hospital</title>', response.content)
        self.assertTrue(response.content.endswith("</html>"))
