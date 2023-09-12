from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('actividades/listado',views.actividades, name='AppMyClub_actividades'),


]