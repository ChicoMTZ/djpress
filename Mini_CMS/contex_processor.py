# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse


def menu(request):
    menu = {'menu': [{'name': 'Entradas', 'url': reverse('Index')},
                     {'name': 'Añadir Entradas', 'url': reverse('agregar')},
                     {'name': 'Páginas', 'url': reverse('Paginas')},
                     {'name': 'Agregar páginas', 'url': reverse('Agregar_p')},
                     {'name': 'Comentarios', 'url': reverse('Comentarios')},
                     {'name': 'Usuarios', 'url': reverse('Usuarios')},
                     {'name': 'Salir', 'url': reverse('Logout')},

                     ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
