from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .forms import SocioForm, LoginForm, Actividad
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


 


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
    print("en vista")
    if request.method == "POST":
        # Instanciamos un formulario con datos
        formulario = SocioForm(request.POST)
        # Validarlo
        if formulario.is_valid():
            # Dar de alta la info

            #ingreso a BBDD
            f_nombre=formulario.cleaned_data['nombre']
            f_apellido=formulario.cleaned_data['apellido']
            f_dni=formulario.cleaned_data['dni']
            f_email=formulario.cleaned_data['email']
            f_direccion=formulario.cleaned_data['direccion']


            try:
                socio = Socio(numero = 1, nombre=f_nombre,apellido=f_apellido,dni=f_dni,email=f_email,direccion=f_direccion)
                socio.save()
            except:
                messages.info(request, "Error al crear el nuevo socio")
            else:
                messages.info(request, "Datos guardados con exito")


            return redirect(reverse("index"))
        
    
    else: #GET

        formulario= SocioForm()
    
    context={
        'alta_socio': formulario

    }

    return render (request, 'core/socio_nuevo.html',context)


def socio_info(request):
    context={
    'noticias' : [
            {'name':'Más info','url_image':'core/img/handball.jpg', 'descrip':'Ascenso en Handball masculino!!'},
            {'name':'Inscripción','url_image':'core/img/colonia.jpg','descrip':'Inscripción verano 2023/2024'},
            {'name':'Ver más','url_image':'core/img/tenis.jpg', 'descrip':'Próximamente torneo...'},
                    ]}
    return render (request,'core/socio_info.html', context)

def portal_socios(request):
    return render(request,'core/portal_socios.html')

class AltaActividad(CreateView):
    model = Actividad
    template_name = 'core/alta_actividad.html'
    success_url = 'listado_actividades'
    # form_class = AltaDocenteModelForm
    fields = '__all__'

class ListaActividades(ListView):
    model = Actividad
    context_object_name = 'listado_actividades'
    template_name = 'core/listado_actividades.html'
    
