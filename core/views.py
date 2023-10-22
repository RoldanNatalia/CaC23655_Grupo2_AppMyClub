from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .forms import SocioForm, LoginForm 
from .models import Persona


 


# Create your views here.
def actividades(request):
    context = {
        'menu_sports' : [
            {'name':'fútbol','url_image':'core/img/pibe_pelota.jpg'},
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
    return render(request,"core/actividades.html",context)

def actividad(request,actividad):
    return render(request,"core/index.html")

def index(request):
    context = {}

    return render(request,"core/index.html",context)

def contacto(request):
    return render(request,'core/contacto.html')

def institucional(request):
    return render(request,'core/institucional.html')

def socios(request):

    if request.method == "POST":

        login_form = LoginForm(request.POST)

        
        if login_form.is_valid():

            messages.info(request, "Ha iniciado sesión correctamente")
            return redirect(reverse('portal_socios'))

    else: 
        login_form = LoginForm()

    context = {
        'ingreso_socios': login_form
    }

    return render (request, 'core/socios.html',context)

def socio_nuevo (request):

    if request.method == "POST":
        # Instanciamos un formulario con datos
        formulario = SocioForm(request.POST)
        # Validarlo
        if formulario.is_valid():
            # Dar de alta la info

            messages.info(request, "Datos enviados con éxito")
        
            

            return redirect(reverse("index"))
        
    
    else: #GET

        formulario= SocioForm()
    
    context={
        'alta_socio': formulario

    }

    return render (request, 'core/socio_nuevo.html',context)

def portal_socios(request):
    return render(request,'core/portal_socios.html')
