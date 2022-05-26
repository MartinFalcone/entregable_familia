from datetime import datetime
from multiprocessing import context
from re import M
from django.http import HttpResponse
from django.shortcuts import render
from appfamilia.models import familia

def familia_template(request):
    familiar_nuevo = familia.objects.create(
    nombre = "liliana", 
    edad = 65, 
    fecha_de_nacimiento = 18/11/1963
    )
    
    context ={"familiar_nuevo":familiar_nuevo}


    return render(request, "familia_template.html", context = context)