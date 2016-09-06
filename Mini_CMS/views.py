# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import *
from Mini_CMS.forms import *
from Mini_CMS.models import Entrada, Pagina
from django.contrib.auth.models import User
from sitio.models import *
from django.http import JsonResponse


@login_required()
def Index(request):
    return render(request, 'index.html')


@method_decorator(login_required, name='dispatch')
class agregar_entradas(CreateView, SuccessMessageMixin):
    template_name = 'añadir_entradas.html'
    model = Entrada
    success_url = '/dj-admin/'
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion']


@method_decorator(login_required, name='dispatch')
class Perfiles(UpdateView):
    model = User
    template_name = 'usuarios/perfiles.html'
    success_url = '/dj-admin/'
    fields = ['first_name', 'last_name', 'email']


@method_decorator(login_required, name='dispatch')
class Editar_Entradas(UpdateView):
    model = Entrada
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion']
    template_name = 'editar_entradas.html'
    success_url = '/dj-admin/'


def login(request):
    template_response = views.login(request, authentication_form=Login_Form,
                                    template_name='usuarios/identificarse.html')
    return template_response


@login_required()
def change_password(request):
    template_response = views.password_change(request, template_name='usuarios/perfiles.html',
                                                  password_change_form=ChancePassword, post_change_redirect='Index')
    messages.info(request, 'Contraseña establecida correctamente')
    return template_response


@login_required()
def logout(request):
    template_response = views.logout(request, next_page='Sitio')
    return template_response


@method_decorator(login_required, name='dispatch')
class Usuarios(ListView):
    model = User
    template_name = 'usuarios/usuarios.html'
    context_object_name = 'usuario_list'


@method_decorator(login_required, name='dispatch')
class Paginas(ListView):
    model = Pagina
    template_name = 'paginas.html'
    context_object_name = 'pagina_list'


@method_decorator(login_required, name='dispatch')
class comentarios(ListView):
    model = Comentario
    template_name = 'comentarios.html'
    context_object_name = 'comentario_list'


@method_decorator(login_required, name='dispatch')
class agregar_paginas(CreateView, SuccessMessageMixin):
    template_name = 'añadir_paginas.html'
    model = Pagina
    success_url = '/dj-admin/paginas'
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion']


@method_decorator(login_required, name='dispatch')
class Editar_Paginas(UpdateView):
    model = Pagina
    fields = ['Autor', 'Titulo', 'Texto', 'Descripcion']
    template_name = 'editar_paginas.html'
    context_object_name = 'Paginas'
    success_url = '/dj-admin/paginas'


@login_required()
def Eliminar_Paginas(request):
    id= request.POST['id_usuario']
    Pagina.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'La página se elminó con satisfactoriamente')
    return JsonResponse({'messages':"Se eliminó el usuario"})

@login_required()
def Eliminar_Comen(request):
    id= request.POST['id_usuario']
    Comentario.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'El comentario se elminó con satisfactoriamente')
    return JsonResponse({'messages':"Se eliminó el usuario"})



@login_required()
def Eliminar_Entradas(request):
    id= request.POST['id_usuario']
    Entrada.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'La entrada se elminó con satisfactoriamente')
    return JsonResponse({'messages':"Se eliminó el usuario"})


@login_required()
def aprovar(request):
    if request.method == 'POST':
        id= request.POST['id_usuario']
        Coment = Comentario.objects.get(pk=id)
        if Coment.Publicado:
            Coment.Publicado = False
            Coment.save()
            messages.add_message(request, messages.SUCCESS, 'La acción se realizó correctamente')
            return JsonResponse({'messages':"Se eliminó el usuario"})
        else:
            Coment.Publicado = True
            Coment.save()
            messages.add_message(request, messages.SUCCESS, 'La acción se realizó correctamente')
            return JsonResponse({'messages':"Se eliminó el usuario"})


@method_decorator(login_required, name='dispatch')
class agregar_usuario(CreateView):
    template_name = 'usuarios/nuevo_usuario.html'
    model = User
    success_url = '/dj-admin/'
    fields = ['username', 'first_name', 'last_name', 'email']


@login_required()
def notificaciones(request):
    return render(request, 'notificaciones.html')
