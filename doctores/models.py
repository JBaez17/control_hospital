from django.db import models


class Doctor(models.Model):
    nombre = models.TextField(default='')
    apellido = models.TextField(default='', blank=True)
