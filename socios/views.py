from django.shortcuts import render, redirect
from django.views.generic import ListView, View,  FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView    
from .forms import CustomPwdChgForm, NuevoPagoForm
from django.http import Http404
from .models import *



# Create your views here.onclick=location.href="{% url 'info_socio' %}"><i class="fas fa-info-circle"></i><span class="m-2">INFORMACION</span>
class Perfil(LoginRequiredMixin, View):
    template_name = "socios/perfil.html"
    model = User
    context_object_name = 'datos_socio'

    def get(self, request):
        context = {
            'socio' : request.user
        }
        return render(request,self.template_name,context)
    
class GrupoFamiliar(Perfil):
    template_name = "socios/grupo_familiar.html"

class HistorialPagos(Perfil):
    template_name = "socios/pagos.html"

    def get(self, request):
        for grupo in request.user.groups.all():
            if "administrador_grupo_f" == grupo.name:
                return super().get(request)
        
        raise Http404

class NoticiasView(ListView):
    model = Comunicado
    template_name = "socios/noticias.html"
    context_object_name = 'noticias'
    ordering = ['-fecha']

class CambiarContra(PasswordChangeView):
    template_name = "socios/cambiar_clave.html"
    form_class = CustomPwdChgForm
    success_url = 'miPerfil'

class NuevoPago(FormView):
    form_class = NuevoPagoForm
    template_name = "socios/nuevo_pago.html"
    success_url = "pagos"

    def get(self, request):
        context = {
            'socio' : request.user,
            'form' : self.form_class
        }
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        nuevo_pago = Pago(grupo = request.user.get_grupo_familiar(), monto = request.user.get_grupo_familiar().balance_mes_actual(), fecha=timezone.now())
        nuevo_pago.save()
        return super().post(self, request, *args, **kwargs)
