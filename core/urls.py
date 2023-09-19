from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('institucional',views.institucional, name='AppMyClub_institucional'),
    path('socios/login',views.socios, name='Socios_login'),
    path('contacto',views.contacto, name='AppMyClub_contacto'),
    path('actividades',views.actividades, name='actividades'),
    path('actividades/<str:actividad>', views.actividad, name="detalle_actividad")

]