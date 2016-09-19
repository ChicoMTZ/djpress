from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Mini_CMS.models import Categoria


@login_required()
def Index(request):
    if Categoria.objects.all().count() == 0:
        Categoria.objects.create(nombre='Epmty')
    return render(request, 'index.html')
