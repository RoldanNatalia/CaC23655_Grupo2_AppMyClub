from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('actividades/',views.actividades, name='AppMyClub_actividades'),
    path('detalle_actividad/<str:deporte>', views.detalle_actividad,name='deporte')
    # path('base/',views.base, name="archivo_base"),
]