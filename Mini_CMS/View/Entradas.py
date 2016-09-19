# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import *
from sitio.models import *
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class agregar_entradas(CreateView, SuccessMessageMixin):
    template_name = 'añadir_entradas.html'
    model = Entrada
    success_url = '/dj-admin/'
    fields = ['Autor', 'Category', 'Titulo', 'Texto', 'Descripcion', 'Fecha']


@method_decorator(login_required, name='dispatch')
class Editar_Entradas(UpdateView):
    model = Entrada
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion', 'Fecha']
    template_name = 'editar_entradas.html'
    success_url = '/dj-admin/'


@login_required()
def Eliminar_Entradas(request):
    id= request.POST['id_usuario']
    Entrada.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'La entrada se elminó con satisfactoriamente')
    return JsonResponse({'messages':"Se eliminó el usuario"})
