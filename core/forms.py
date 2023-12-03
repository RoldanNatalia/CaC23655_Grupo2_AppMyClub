from django import forms

class LoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario:", required=True, widget=forms.TextInput(
                              attrs={'class': "form-outline mb-4"}))
    clave = forms.CharField(label="Contraseña",widget=forms.PasswordInput, required=False)
