from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("Bienvenidos al Sistema Gestión para clubes")

def actividades (request):
    return HttpResponse("""
<ul>
    <li>Futbol</li>
    <li>Vóley</li>
    <li>Patín</li>
</ul> 
""")
                        
def index(request):
    context = {
        'menu_activities' : [
            {'name':'Futbol','url_image':'core/img/pibe_pelota.jpg'},
            {'name':'Voley','url_image':'core/img/volley.jpg'},
            {'name':'Basket','url_image':'core/img/basketball.jpg'},
            {'name':'Tenis','url_image':'core/img/tenis.jpg'},
            {'name':'Natacion','url_image':'core/img/natacion.jpg'},
            {'name':'Handball','url_image':'core/img/handball.jpg'}
        ]
    }

    return render(request,"core/index.html",context)

