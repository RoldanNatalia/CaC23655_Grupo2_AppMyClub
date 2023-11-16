from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('institucional',views.institucional, name='AppMyClub_institucional'),
    path('actividades',views.actividades, name='actividades'),
    path('actividades/<str:actividad>', views.actividad, name="detalle_actividad"),
    path('contacto',views.contacto,name="core-contacto"),
    path('listado_actividades',views.ListaActividades.as_view(),name="lista_actividad"),
    path('socios/nuevo',views.socio_nuevo,name="nuevo_socio"),
    path('socios/login',views.loginView, name='Socios_login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('Portal-socios',views.info_socio,name="info_socio"),
    path('Portal-socios/reclamo', views.reclamo_socio, name="reclamo_socio"),
    path('Portal-socios/info', views.info_socio, name="info_socio")
    # path('Portal-socios/reservas',views.reservas,name="reservas_socio"),

]