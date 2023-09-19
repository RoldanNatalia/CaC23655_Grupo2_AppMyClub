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

def login (request):
    return render (request, "core/login.html")


