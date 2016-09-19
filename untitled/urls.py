from django.conf.urls import url, include
from django.contrib import admin
from sitio.views import *
from Mini_CMS.views import *
from Mini_CMS.ajax import *
from Mini_CMS.View.Entradas import *
from Mini_CMS.View.Paginas import *
from Mini_CMS.View.User import *
from Mini_CMS.View.Comentarios import *
from Mini_CMS.View import *


extra_patterns = [

    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^', include('sitio.url')),

    ]

urlpatterns = extra_patterns + [

    url(r'^dj-admin/$', Index, name='Index'),

    url(r'^accounts/login/$', login, name='Login'),
    url(r'^accounts/logout/$', logout, name='Logout'),


    url(r'^dj-admin/agregar/$', agregar_entradas.as_view(), name='agregar'),
    url(r'^dj-admin/editar_entradas/([0-9]{4})-([0-9]{2})-([0-9]+)/(?P<pk>[\w-]+)/$', Editar_Entradas.as_view(model=Entrada), name='Editar_Entradas'),
    url(r'^dj-admin/eliminar_entradas/$', Eliminar_Entradas, name='Eliminar_Entradas'),


    url('^dj-admin/usuarios/$', Usuarios.as_view(), name='Usuarios'),
    url('^dj-admin/editar_perfil/$', change_password, name='Editar_Perfil'),
    url(r'^dj-admin/perfiles/(?P<pk>[\w-]+)/$', Perfiles.as_view(model=User), name='Perfiles'),
    url('^dj-admin/agregar_usuario/$', agregar_usuario.as_view(), name='Agregar_Usuarios'),

    url(r'^dj-admin/paginas/$', Pages.as_view(), name='Paginas'),
    url(r'^dj-admin/agregar_paginas/$', agregar_paginas.as_view(), name='Agregar_p'),
    url(r'^dj-admin/editar_paginas/([0-9]{4})-([0-9]{2})-([0-9]+)/(?P<pk>[\w-]+)/$', Editar_Paginas.as_view(model=Pagina), name='Editar_Paginas'),
    url(r'^dj-admin/eliminar_paginas/$', Eliminar_Paginas, name='Eliminar_Paginas'),


    url(r'^ajax/get_entradas/$', get_entradas, name='get_entradas'),
    url(r'^ajax/get_paginas/$', get_paginas, name='get_paginas'),
    url(r'^ajax/get_comentarios/$', get_comentarios, name='get_comentarios'),
    url(r'^ajax/filtrado_categorias/(?P<pk>[\w-]+)/$', filtrado_categorias, name='filtrado_categorias'),


    url(r'^dj-admin/comentarios/$', comentarios.as_view(), name='Comentarios'),
    url(r'^dj-admin/eliminar_comentarios/$', Eliminar_Comen, name='Eliminar_Comen'),
    url(r'^dj-admin/aprovar/$', aprovar, name='Aprovar_Coment'),


    url(r'^notificaciones/$', notificaciones, name='notificaciones'),
]