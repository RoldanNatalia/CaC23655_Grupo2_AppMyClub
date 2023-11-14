from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import NumberInput
import re
from .models import Actividad

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



class LoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario:", required=True)
    contraseña = forms.CharField(label="Contraseña",widget=forms.PasswordInput, required=False)

    def clean_nombre(self):
       
       # if self.cleaned_data["nombre"].isalpha()==False:
        #    raise ValidationError("Debe ingresar solo letras, sin espacios")
        
        
        return self.cleaned_data["nombre"]
    
    
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')

        #if len(contraseña) != 6:
         #   raise forms.ValidationError("La contraseña debe tener exactamente 6 caracteres.")

        return contraseña
    
#class Actividad(forms.ModelForm):
 #   class Meta:
  #      model: Actividad
   #     fields = '__all__'

class ReclamoForm (forms.Form):
    nombre= forms.CharField(label="Nombre*:", required=True, max_length=50)
    email= forms.EmailField(label="Email*:", required = True)
    telefono= forms.IntegerField(label="Teléfono:",required=False)
    consulta= forms.CharField(label="Mensaje*:", max_length=250, required=True, widget=forms.Textarea)

    





