# from datetime import datetime
# from multiprocessing import context
# from re import M
# from django.http import HttpResponse
from django.shortcuts import render
from appfamilia.models import familia

def familia_template(request):
    familiar_uno = familia.objects.create(
    nombre = "Liliana", 
    edad = 65, 
    fecha = "1963-11-18"
    )
    context ={"familiar_uno":familiar_uno}
    
    
    # familiar_dos = familia.objects.create(
    # nombre = "Rocio", 
    # edad = 32, 
    # # fecha_de_nacimiento = "1989-29-05"
    # )
    # context ={"familiar_dos":familiar_dos}


    return render(request, "familia_template.html", context = context)