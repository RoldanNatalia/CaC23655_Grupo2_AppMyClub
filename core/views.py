from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 


# Create your views here.
def index (request):
    return render(request, "core/index.html")

def actividades (request):
    return render (request, "core/actividades.html")

def institucional (request):
    return render (request, "core/institucional.html")

def socios (request):
    return render (request,"core/socios.html")

def contacto (request):
    return render (request, "core/contacto.html")