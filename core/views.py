from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 


# Create your views here.
def index(request):
    context = {
        'menu_sports' : [
            {'name':'futbol','url_image':'core/img/pibe_pelota.jpg'},
            {'name':'voley','url_image':'core/img/volley.jpg'},
            {'name':'basket','url_image':'core/img/basketball.jpg'},
            {'name':'tenis','url_image':'core/img/tenis.jpg'},
            {'name':'natación','url_image':'core/img/natacion.jpg'},
            {'name':'handball','url_image':'core/img/handball.jpg'}
        ],
        'menu_activities' : [
            {'name':'yoga','url_image':'core/img/yoga.jpg'},
            {'name':'expresión','url_image':'core/img/expresion.jpeg'},
            {'name':'parrilla','url_image':'core/img/parrilla.jpeg'},
            {'name':'colonia','url_image':'core/img/colonia.jpg'},
            {'name':'eventos','url_image':'core/img/recital.jpg'},
            {'name':'salón','url_image':'core/img/salon.jpeg'}
        ]
    }

    return render(request,"core/index.html",context)

def actividades (request):
    return HttpResponse("""
<ul>
    <li>Futbol</li>
    <li>Vóley</li>
    <li>Patín</li>
</ul> 
""")

def actividad(request,actividad):
    return HttpResponse(f"Pagina de {actividad}")

def socios (request):
    return render (request,"core/socios.html")

def contacto (request):
    return render (request, "core/contacto.html")

def institucional (request):
    return render (request, "core/institucional.html")