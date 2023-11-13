from django.contrib import admin
from core.models import Socio, Profesor, Curso, Predio, Actividad, Inscripcion, DiaCurso, Dia

#Register your models here.

class SocioAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','apellido','dni','direccion')
    list_editable = ('nombre','apellido','dni','direccion')

admin.site.register(Socio, SocioAdmin)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Predio)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(DiaCurso)
# admin.site.register(Dia)



