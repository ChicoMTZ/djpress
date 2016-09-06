from django.conf.urls import url
from sitio.views import *

urlpatterns = [
    url(r'^$', sitio.as_view(), name="Sitio"),
    url(r'^entradas_details/(?P<pk>[\w-]+)/$', Entradas_Details.as_view(), name="Entradas_Details"),
    url(r'^validar/$', validar, name="Validar"),

    url(r'^pagina_details/(?P<pk>[\w-]+)/$', Pagina_Details.as_view(), name="Pagina_Details"),

]
