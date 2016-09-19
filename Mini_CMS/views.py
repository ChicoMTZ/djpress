# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def notificaciones(request):
    return render(request, 'notificaciones.html')
