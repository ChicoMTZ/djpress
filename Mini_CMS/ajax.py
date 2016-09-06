from django.http import JsonResponse
from Mini_CMS.models import Entrada, Pagina
from sitio.models import Comentario

def get_entradas(request):
    elementos = []
    usuarios = Entrada.objects.all()
    for usuario in usuarios:
        elementos.append(usuario.json())
    response = {'aaData': elementos}
    return JsonResponse(response)


def get_paginas(request):
    elementos = []
    usuarios = Pagina.objects.all()
    for usuario in usuarios:
        elementos.append(usuario.json())
    response = {'aaData': elementos}
    return JsonResponse(response)


def get_comentarios(request):
    elementos = []
    usuarios = Comentario.objects.all()
    for usuario in usuarios:
        elementos.append(usuario.json())
    response = {'aaData': elementos}
    return JsonResponse(response)
