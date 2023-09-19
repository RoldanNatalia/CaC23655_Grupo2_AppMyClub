from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("Bienvenidos al Sistema Gestión para clubes")

def actividades (request):

    listado_actividades=['fútbol','basquet','voley','patín','taekwondo','gimnasia','pileta']

    context={
        'lista_actividades' : listado_actividades
        }
    
    return render(request,"core/actividades.html",context)

def detalle_actividad(request, deporte):
    context={
        'actividad': deporte
    }
    return render (request,"core/detalle_actividad.html",context)

# def base(request):
#     return render(request, "core/base.html")

