# -*- coding: UTF-8 -*-
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Entrada(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=200)
    Texto = RichTextField(verbose_name=_("Texto"))
    Descripcion = models.CharField(max_length=200)
    Fecha = models.DateTimeField('Fecha de publicación', auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.Autor.username + ' --- ' + self.Titulo

    def json(self):
        return [self.pk, self.Titulo, self.Autor.username, self.comentario_set.count(), self.pk, self.Autor.pk]


class Pagina(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=200)
    Texto = RichTextField(verbose_name=_("Texto"))
    Descripcion = models.CharField(max_length=200)
    Fecha = models.DateTimeField('Fecha de publicación', auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.Autor.username

    def json(self):
        return [self.pk, self.Titulo, self.Autor.username, self.pk, self.Autor.pk]
