# -*- coding: UTF-8 -*-
from django.views.generic import *
from Mini_CMS.models import *
from .forms import Comentarios_Form
from django_ajax.decorators import ajax
from sitio.models import Comentario
from django.utils import timezone
from django.contrib import messages


class sitio(ListView):
    model = Entrada
    template_name = 'sitio.html'
    context_object_name = 'entrada_list'

    def get_context_data(self, **kwargs):
        context = super(sitio, self).get_context_data(**kwargs)
        context['paginas'] = Pagina.objects.all()
        return context


class Entradas_Details(DetailView):
    model = Entrada
    template_name = 'entradas_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Entradas_Details, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ids']=(self.kwargs['pk'])
        yu = Entrada.objects.get(pk=self.kwargs['pk'])
        context['List_Coment'] = yu.comentario_set.all()
        context['forms'] = Comentarios_Form

        return context


class Pagina_Details(DetailView):
    model = Pagina
    template_name = 'paginas_details.html'


@ajax
def validar(request):
    if request.method == 'POST':
        forms = Comentarios_Form(request.POST)
        if forms.is_valid():
            nombre = request.POST.get('Nombre', '')
            emails = request.POST.get('Correo', '')
            Texto = request.POST.get('Texto', '')
            url = int(request.POST.get('url', ))
            Coment = Comentario(Nombre=nombre, Correo=emails, Texto=Texto, Publicado=False, Entrada=Entrada.objects.get(pk=url), Fecha=timezone.now())
            Coment.save()
            messages.add_message(request, messages.SUCCESS, 'El comentario se envió correctamente. Necesita la aprovación de un Administrador')
            return {
            'inner-fragments': {
                '.notificaciones': '<script>recargarMensajes();</script>'

             },
                   }
