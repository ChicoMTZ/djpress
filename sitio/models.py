# -*- coding: UTF-8 -*-
from django.db import models
from Mini_CMS.models import Entrada


class Comentario(models.Model):
    Entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    Correo = models.EmailField()
    Nombre = models.CharField(max_length=200)
    Texto = models.TextField()
    Fecha = models.DateTimeField('Fecha de publicación', auto_now_add=True)
    Publicado = models.BooleanField()

    def json(self):
        return [self.Nombre, self.Texto, self.Entrada.Titulo, self.Publicado, self.Entrada.pk, self.pk]

    def __str__(self):              # __unicode__ on Python 2
        return self.Nombre

