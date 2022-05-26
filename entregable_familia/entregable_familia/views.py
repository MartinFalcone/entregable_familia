from datetime import datetime
from multiprocessing import context
from re import M
from django.http import HttpResponse
from django.shortcuts import render

def familia_template(request):
    context ={
        "familiar1": "lialiana",
        "familiar2": "rolando",
        "familiar3": "rocio",
    } 

    return render(request, "familia_template.html", context = context)








