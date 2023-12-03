from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput

class CustomPwdChgForm(PasswordChangeForm):
    old_password = forms.CharField(widget=TextInput(attrs={'placeholder': 'Contraseña anterior', 'class':'form-control'}))
    new_password1 = forms.CharField(widget=TextInput(attrs={'placeholder': 'Nueva contraseña', 'class':'form-control'}))
    new_password2 = forms.CharField(widget=TextInput(attrs={'placeholder': 'Repetir nueva contraseña', 'class':'form-control'}))

class NuevoPagoForm(forms.Form):
    numero_tarjeta = forms.CharField(min_length=16,max_length=16,widget=TextInput(attrs={'placeholder': 'ej: 4141 4242 4343 4444', 'class':'form-control'}))
    nombre = forms.CharField(min_length=0,max_length=50,widget=TextInput(attrs={'placeholder': 'juan Perez', 'class':'form-control'}))
    codigo = forms.CharField(max_length=3, min_length=3, widget=PasswordInput(attrs={'placeholder':'123','class':'form-control'}))