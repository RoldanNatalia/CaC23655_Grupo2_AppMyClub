from collections.abc import Mapping
from typing import Any
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from .models import *


#Register your models here.
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(DiaCurso)
admin.site.register(GrupoFamiliar)
admin.site.register(SocioGrupo)
admin.site.register(Pago)
admin.site.register(Categoria)
admin.site.register(Comunicado)



admin.site.index_title = "Tablas"
admin.site.site_header = "Administración del clu"
admin.site.site_title = "El super clú"


'''agregar comunicado junto con cambio de mensualidad'''
@admin.register(CambioMensualidadFija)
class CambioMensualidad(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.save()
        cuerpo = obj.get_comunicado()
        titulo = "Cambio de mensualidad fija"
        seccion = Categoria.objects.get(id=2)
        comunicado = Comunicado(titulo=titulo,cuerpo=cuerpo,seccion=seccion,fecha=obj.fecha)
        comunicado.save()
        return

'''agregar un curso con solo docentes como opcion'''
@admin.register(Curso)
class AgregarCurso(admin.ModelAdmin):
    def get_form(self, request, *args, **kwargs):
        form = super(AgregarCurso, self).get_form(request, *args, **kwargs)
        form.base_fields['docente'].queryset = User.objects.filter(groups__name='docente')
        return form
    
'''agregar alumno a curso desde docente'''
@admin.register(Inscripcion)
class InscripcionAlumno(admin.ModelAdmin):

    def get_form(self, request, *args, **kwargs):
        form = super(InscripcionAlumno, self).get_form(request, *args, **kwargs)
        if request.user.is_superuser :
            qs = Curso.objects.all()
        else:
            qs = Curso.objects.filter(docente=request.user)
        form.base_fields['curso'].queryset = qs
        return form


'''Agregar socio a grupo familiar existente'''
class AgregarSocioForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(GrupoFamiliar.objects)
    es_docente = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name','dni','direccion','email']


@admin.register(User)
class SocioAdmin(admin.ModelAdmin):
    form = AgregarSocioForm
    list_display = ('username', 'first_name', 'last_name', 'dni', 'email', 'direccion')

    def save_model(self, request, obj, form, change):
        #modifico el username y guardo el usuario
        obj.username = username=form.cleaned_data['dni']
        obj.set_password(form.cleaned_data['dni'])      

        #si es docente le doy ser staff
        if form.cleaned_data['es_docente']:
            obj.is_staff = True

        super().save_model(request, obj, form, change)

        if form.cleaned_data['es_docente']:
            grupo_docente = Group.objects.get(name='docente') 
            grupo_docente.user_set.add(obj)

        #si existe el grupo familiar añado al usuario de otra forma creo uno nuevo
        if form.cleaned_data['grupo'].nombre == "nueva":
            permisos = Group.objects.get(name='administrador_grupo_f') 
            permisos.user_set.add(obj)

            grupo_familiar = GrupoFamiliar(nombre=form.cleaned_data['last_name'])
            grupo_familiar.save()
        else:
            permisos = Group.objects.get(name='integrante_grupo_f') 
            permisos.user_set.add(obj)
            grupo_familiar = form.cleaned_data['grupo']

        nuevo_socio_grupo =  SocioGrupo(grupo = grupo_familiar, socio = obj)
        nuevo_socio_grupo.save()