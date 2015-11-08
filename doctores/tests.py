from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from doctores.models import Doctor

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
        """self.assertEqual(response.content.decode(), expected_html)
        self.assertIn('Juan', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'nuevo_doctor':  'Juan'})"""

        self.assertEqual(response.content.decode(), expected_html)

    def test_pagina_principal_puede_guardar_una_peticion_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['nombre_doc'] = 'Juan'

        response = home_page(request)

        # self.assertIn('Nuevo Doctor', response.content.decode())
        self.assertEqual(Doctor.objects.count(), 1)
        nuevo_doctor = Doctor.objects.first()
        self.assertEqual(nuevo_doctor.nombre, 'Juan')
        """expected_html = render_to_string(
            'home.html',
            {'nuevo_doctor': 'Juan'})
        self.assertEqual(response.content.decode(), expected_html)"""

    def test_pagina_principal_redirecciona_despues_de_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['nombre_doc'] = 'Juan'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/la-unica-lista-en-el-mundo/')

    def test_pagina_principal_solo_guarda_cuando_es_necesario(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Doctor.objects.count(), 0)


class TestModelDoctores(TestCase):

    def test_guardando_y_obteniendo_dactores(self):
        primer_doctor = Doctor()
        primer_doctor.nombre = 'Juan'
        primer_doctor.save()

        segundo_doctor = Doctor()
        segundo_doctor.nombre = 'Pedro'
        segundo_doctor.save()

        doctores_guardados = Doctor.objects.all()
        self.assertEqual(doctores_guardados.count(), 2)

        primer_doctor_guardado = doctores_guardados[0]
        segundo_doctor_guardado = doctores_guardados[1]
        self.assertEqual(primer_doctor_guardado.nombre, 'Juan')
        self.assertEqual(segundo_doctor_guardado.nombre, 'Pedro')


class TestVistaListas(TestCase):

    def test_mostrar_todos_elementos(self):
        Doctor.objects.create(nombre='Juan')
        Doctor.objects.create(nombre='Pedro')

        response = self.client.get('/lists/la-unica-lista-en-el-mundo/')

        self.assertContains(response, 'Juan')
        self.assertContains(response, 'Pedro')

    def test_se_usa_un_template_para_lista(self):
        response = self.client.get('/lists/la-unica-lista-en-el-mundo/')
        self.assertTemplateUsed(response, 'list.html')
