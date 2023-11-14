from django.contrib import admin
from django import forms
from core.models import Socio, Profesor, Curso, Predio, Actividad, Inscripcion, DiaCurso, Dia, User


#Register your models here.
admin.site.register(Curso)
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(DiaCurso)
admin.site.register(Dia)


admin.site.index_title = "Tablas"
admin.site.site_header = "Administración del clu"
admin.site.site_title = "El super clú"


'''Aquí se crea un usuario con username y password igual al valor del dni de un nuevo socio'''
class SocioForm(forms.ModelForm):
    dni=forms.CharField(max_length=8)
    email = forms.EmailField()

    class Meta:
        model = Socio
        exclude = ["usuario"]


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm
    # list_display = ('usuario', 'nombre', 'apellido', 'dni',)
    # list_editable = ('usuario', 'nombre', 'apellido', )
    #inlines = [UserAdmin]

    def save_model(self, request, obj, form, change):
        dni = form.cleaned_data["dni"]
        correo = form.cleaned_data['email']
        usuario, _ = User.objects.get_or_create(username=dni,password=dni,email=correo)
        obj.usuario = usuario
        super().save_model(request, obj, form, change)


'''Lo mismo para un profesor pero con su actividad'''
class ProfesorForm(forms.ModelForm):
    dni=forms.CharField(max_length=8)
    email = forms.EmailField()


    class Meta:
        model = Profesor
        exclude = ["usuario"]


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    form = ProfesorForm

    def save_model(self, request, obj, form, change):
        dni = form.cleaned_data["dni"]
        correo = form.cleaned_data['email']
        usuario, _ = User.objects.get_or_create(username=dni,password=dni,email=correo)
        obj.usuario = usuario
        super().save_model(request, obj, form, change)