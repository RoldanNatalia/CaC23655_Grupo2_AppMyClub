from django import forms
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario:", required=True)
    contraseña = forms.CharField(label="Contraseña",widget=forms.PasswordInput, required=False, max_length=6)

    def clean_nombre(self):
       
        if self.cleaned_data["nombre"].isalpha()==False:
            raise ValidationError("Debe ingresar solo letras, sin espacios")
        
        
        return self.cleaned_data["nombre"]
    
    
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')

        if len(contraseña) != 6:
            raise forms.ValidationError("La contraseña debe tener exactamente 6 caracteres.")

        return contraseña



    

    
        
    