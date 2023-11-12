from django.contrib import admin
from core.models import Socio, Profesor, Curso, Predio, Actividad, Inscripcion, DiaCurso

# Register your models here.

# class SocioAdmin(admin.ModelAdmin):
#     list_display = ('nombre','apellido','dni','email','direccion')
#     list_editable = ('nombre','apellido','dni','email','direccion')

admin.site.register(Socio, )
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(DiaCurso)



