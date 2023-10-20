from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('institucional',views.institucional, name='AppMyClub_institucional'),
    path('actividades',views.actividades, name='actividades'),
    path('actividades/<str:actividad>', views.actividad, name="detalle_actividad"),
    #path('contacto',views.contacto, name='AppMyClub_contacto'),
    path('contacto',views.contacto,name="core-contacto"),
    path('socios/nuevo',views.socio_nuevo,name="nuevo_socio"),
    path('socios/login',views.socios, name='Socios_login'),
    path('Portal-socios',views.portal_socios,name="portal_socios"),
    
]