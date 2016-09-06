# -*- coding: utf-8 -*-
from django import forms
from sitio.models import Comentario


class Comentarios_Form(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['Nombre', 'Correo', 'Texto']
