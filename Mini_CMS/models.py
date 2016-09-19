# -*- coding: UTF-8 -*-
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Categoria(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):  # __unicode__ on Python 2
        if self.nombre == '':
            return 'Empty'
        else:
            return self.nombre


class Entrada(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().username)
    Category = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=_(Categoria.objects.first().nombre))
    Titulo = models.CharField(max_length=200, blank=True)
    Texto = RichTextField(verbose_name=_("Texto"))
    Descripcion = models.CharField(max_length=200)
    Fecha = models.DateField('Fecha de publicación')

    def __str__(self):  # __unicode__ on Python 2
        return self.Autor.username + ' --- ' + self.Titulo

    def json(self):
        return [self.Fecha, self.Titulo, self.Autor.username, self.comentario_set.count(), self.pk, self.Autor.pk, self.Category.nombre, self.Category.pk]


class Pagina(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=200)
    Texto = RichTextField(verbose_name=_("Texto"))
    Descripcion = models.CharField(max_length=200)
    Fecha = models.DateField('Fecha de publicación')

    def __str__(self):              # __unicode__ on Python 2
        return self.Autor.username

    def json(self):
        return [self.pk, self.Titulo, self.Autor.username, self.Autor.pk, self.Fecha]
