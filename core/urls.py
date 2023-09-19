from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('actividades',views.actividades, name='actividades'),
    path('actividades/<str:actividad>', views.actividad, name="detalle_actividad")

]