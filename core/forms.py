from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import NumberInput
import re
from .models import *

class SocioForm(forms.Form):
    nombre= forms.CharField(label="Nombre:", required=True)
    apellido= forms.CharField(label="Apellido:", required=True)
    dni=forms.CharField(label="DNI:", max_length=8, required=True)
    FecNac=forms.DateField(label="Fecha de nacimiento:",widget=NumberInput(attrs={'type': 'date'}))
    email= forms.EmailField(label="Email:",required=True)
    direccion=forms.CharField(label="Dirección:",max_length=100)
    

    def clean_nombre(self):
        #nombre = self.cleaned_data['nombre']
        if not self.cleaned_data['nombre'].isalpha():
            raise forms.ValidationError('El nombre no puede contener números')
        return self.cleaned_data['nombre']
    

    def clean_dni(self):
            
        #regex = r'^ \ d {1,2} \.? \ d {3} \.? \ d {3} $'#r'^\d{7}\d?$'
        regex = '[0-9]{8}'
        
        if not(re.match(regex,self.cleaned_data['dni'])):
            
            raise forms.ValidationError('DNI erróneo')
        
        return self.cleaned_data['dni']
    


# class ReservaForm(forms.Form):
#     predios = []
#     for predio in Predio.objects.all():
#         predios.append((predio,predio.nombre))

#     predio = forms.ChoiceField(choices=predios)
#     fecha = forms.DateField(widget=forms.SelectDateWidget())
#     desde_hora = forms.ChoiceField(label="Desde", choices=[(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20)])
#     desde_minutos = forms.ChoiceField(label=":",choices=[(0,"00"),(0.25,"15"),(0.5,"30"),(0.75,"45")])

#     ejemplo = forms.DateField()
    
#     def clean_horario():
#         pass

class LoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario:", required=True)
    clave = forms.CharField(label="Contraseña",widget=forms.PasswordInput, required=False)

    def clean_nombre(self):
       
        # if self.cleaned_data["nombre"].isalpha()==False:
        #     raise ValidationError("Debe ingresar solo letras, sin espacios")
        
        
        return self.cleaned_data["nombre"]
    
    
    def clean_contraseña(self):
        clave = self.cleaned_data.get('contraseña')

        # if len(clave) != 6:
        #     raise forms.ValidationError("La contraseña debe tener exactamente 6 caracteres.")

        return clave
    
# class Actividad(forms.ModelForm):
#     class Meta:
#         model: Actividad
#         fields = '__all__'

# class NuevoPredioForm(forms.Form):
#     nombre = forms.CharField(label="nombre del predio:")

    



