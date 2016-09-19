from django.conf.urls import url
from sitio.views import *

urlpatterns = [
    #TODO: Arreglar las expresiones regulares
    url(r'^$', sitio.as_view(), name="Sitio"),
    url(r'^entradas_details/(?P<Fecha>[0-9]{4}-[0-9]{2}-[0-9]+)/(?P<pk>[\w-]+)/$', Entradas_Details.as_view(), name="Entradas_Details"),
    url(r'^validar/$', validar, name="Validar"),

    url(r'^pagina_details/(?P<Fecha>[0-9]{4}-[0-9]{2}-[0-9]+)/(?P<pk>[\w-]+)/$', Pagina_Details.as_view(), name="Pagina_Details"),

]
