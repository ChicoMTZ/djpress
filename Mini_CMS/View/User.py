# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import *
from Mini_CMS.forms import *
from django.contrib.auth.models import User


@method_decorator(login_required, name='dispatch')
class Perfiles(UpdateView):
    model = User
    template_name = 'usuarios/perfiles.html'
    success_url = '/dj-admin/'
    fields = ['first_name', 'last_name', 'email']


def login(request):
    template_response = views.login(request, authentication_form=Login_Form,
                                    template_name='usuarios/identificarse.html')
    return template_response


@login_required()
def logout(request):
    template_response = views.logout(request, next_page='Sitio')
    return template_response


@login_required()
def change_password(request):
    template_response = views.password_change(request, template_name='usuarios/perfiles.html',
                                                  password_change_form=ChancePassword, post_change_redirect='Index')
    messages.info(request, 'Contraseña establecida correctamente')
    return template_response


@method_decorator(login_required, name='dispatch')
class Usuarios(ListView):
    model = User
    template_name = 'usuarios/usuarios.html'
    context_object_name = 'usuario_list'


@method_decorator(login_required, name='dispatch')
class agregar_usuario(CreateView):
    template_name = 'usuarios/nuevo_usuario.html'
    model = User
    success_url = '/dj-admin/'
    fields = ['username', 'first_name', 'last_name', 'email']
