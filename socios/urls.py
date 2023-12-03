from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('', views.Perfil.as_view(), name='socio-perfil'), 
    path('grupo',views.GrupoFamiliar.as_view(), name='socio-grupo_familiar'),
    path('logout', LogoutView.as_view(), name='socio-logout'),
    path('pagos', views.HistorialPagos.as_view(),name="socio-pagos"),
    path('nueva_clave', views.CambiarContra.as_view(success_url=reverse_lazy('socio-perfil')), name='socio-cambiar-clave'),
    path('nuevo_pago', views.NuevoPago.as_view(), name="socio-pagar"),
    path('noticias', views.NoticiasView.as_view(), name="noticias")

]