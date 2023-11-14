from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('institucional',views.institucional, name='AppMyClub_institucional'),
    path('actividades',views.actividades, name='actividades'),
    path('actividades/<str:actividad>', views.actividad, name="detalle_actividad"),
    #path('contacto',views.contacto, name='AppMyClub_contacto'),
    path('contacto',views.contacto,name="core-contacto"),
    path('socios/nuevo',views.socio_nuevo,name="nuevo_socio"),
    path('socios/login',views.loginView, name='Socios_login'),
    path('Portal-socios',views.portal_socios,name="portal_socios"),
    path('Portal-socios/info',views.socio_info,name="info_socio"),
    path('Portal-socios/reclamos',views.socio_reclamo,name="reclamo_socio"),
    #path('alta_actividad',views.AltaActividad.as_view(),name="alta_actividad"),
    path('listado_actividades',views.ListaActividades.as_view(),name="lista_actividad"),
    path('accounts/logout/', views.logout_view, name='logout'),
    # path('Portal-socios/reservas',views.reservas,name="reservas_socio"),


]