# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from Mini_CMS.models import Pagina
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class Pages(ListView):
    model = Pagina
    template_name = 'paginas.html'
    context_object_name = 'pagina_list'


@method_decorator(login_required, name='dispatch')
class agregar_paginas(CreateView, SuccessMessageMixin):
    template_name = 'añadir_paginas.html'
    model = Pagina
    success_url = '/dj-admin/paginas'
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion', 'Fecha']


@method_decorator(login_required, name='dispatch')
class Editar_Paginas(UpdateView):
    model = Pagina
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion', 'Fecha']
    template_name = 'editar_paginas.html'
    context_object_name = 'Paginas'
    success_url = '/dj-admin/paginas'


@login_required()
def Eliminar_Paginas(request):
    id= request.POST['id_usuario']
    Pagina.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'La página se elminó con satisfactoriamente')
    return JsonResponse({'messages':"Se eliminó el usuario"})
