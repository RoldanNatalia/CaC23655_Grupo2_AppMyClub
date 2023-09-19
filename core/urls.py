from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('institucional',views.institucional, name='AppMyClub_institucional'),
    path('actividades/listado',views.actividades, name='AppMyClub_actividades'),
    path('socios/login',views.socios, name='Socios_login'),
    path('contacto',views.contacto, name='AppMyClub_contacto'),

]