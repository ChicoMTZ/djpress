# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import *
from sitio.models import Comentario
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class comentarios(ListView):
    model = Comentario
    template_name = 'comentarios.html'
    context_object_name = 'comentario_list'


@login_required()
def Eliminar_Comen(request):
    id= request.POST['id_usuario']
    Comentario.objects.get(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'El comentario se elminó con satisfactoriamente')
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
