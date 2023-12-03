from datetime import date
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    direccion = models.CharField(max_length=100, default='n/a')
    dni = models.CharField(max_length=8, default='11111111')

    def clean_dni(self):
        if not self.cleaned_data['dni'].isnumeric():
            raise ValidationError("El dni debe ser numerico")

        return self.cleaned_data['dni']
    
    def __str__(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} - {self.dni};"
    
    def get_mensualidad_movil(self):
        suma = 0

        for actividad in self.get_actividades():
            suma += actividad.mensualidad
    
        return suma
    
    def get_mensualidad_fija(self):
        return CambioMensualidadFija.objects.last().monto

    def get_actividades(self):
        return Curso.objects.filter(alumnos = self)
    
    def get_grupo_familiar(self):
        return SocioGrupo.objects.get(socio = self).grupo
    

class Actividad(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural = "actividades"
    
class Predio(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Dia(models.Model):
    dia = models.CharField(max_length=9, unique=True)

    def __str__(self) -> str:
        return self.dia

    def clean_dia(self):
        if not self.cleaned_data['dia'] in ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]:
            raise ValidationError("Dia no pertenece al calendario") 

        return self.cleaned_data['dia']
    

class Curso(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    docente = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1, related_name='docente_de_curso')
    alumnos = models.ManyToManyField(User, through="Inscripcion")
    dias = models.ManyToManyField(Dia, through="DiaCurso")
    desde = models.FloatField()
    hasta = models.FloatField()
    predio = models.ForeignKey(Predio, on_delete=models.DO_NOTHING)
    mensualidad = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.actividad} en {self.predio} dias {[i.dia for i in self.dias.all()]}"

    def clean_horario(self):
        if not(0 < self.cleaned_data['desde'] < 24 and 0 < self.cleaned_data['hasta'] < 24 ):
            raise ValidationError("Fechas incorrectas no cumplen formato de 24hs")
        if not(self.cleaned_data['desde'] < self.cleaned_data['hasta']):
            raise ValidationError("El inicio debe ser menor que el final de la clase")
    
    def clean_mensualidad(self):
        if self.cleaned_data['mensualidad'] < 0:
            raise ValidationError("La mensualidad no puede ser negativa")

        return self.cleaned_data['mensualidad']
    
    def get_dias(self):
        cadena = ""
        for dia in self.dias.all():
            cadena += f" {dia.dia}"

        return cadena
    
    def get_horario(self):
        horas = [str(int(self.desde)),str(int(self.hasta))]
        for i in range(len(horas)):
            if len(horas[i]) == 1:
                horas[i] = "0" + horas[i]

        minutos = [str(int(self.desde*60 % 60)),str(int(self.hasta*60 % 60))]
        for i in range(len(minutos)):
            if len(minutos[i]) == 1:
                minutos[i] = minutos[i] + "0"


        return {'desde':f'{horas[0]}:{minutos[0]}','hasta':f'{horas[1]}:{minutos[1]}'}

class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self) -> str:
        return f"inscripcion de {self.curso.actividad} en {self.curso.predio} del alumno {self.alumno}"

    class Meta:
        verbose_name_plural = "inscripciones"

class DiaCurso(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"clase de {self.curso.actividad} en {self.curso.predio} el dia {self.dia}"
    

#grupo familiar y pagos
class GrupoFamiliar(models.Model):
    nombre = models.CharField(max_length=50)
    integrantes = models.ManyToManyField(User, through="SocioGrupo")

    def __str__(self) -> str:
        return f'Familia {self.nombre} {str([i.first_name for i in self.integrantes.all()])}'
    
    class Meta:
        verbose_name_plural = "grupos familiares"

    def cuota_movil_total(self):
        total = 0
        for integrante in self.integrantes.all():
            total += integrante.get_mensualidad_movil()
        return total

    def cuota_fija_total(self):
        return CambioMensualidadFija.objects.last().monto * self.integrantes.count()

    def get_historial_pagos(self):
        return Pago.objects.filter(grupo = self).order_by('-fecha')
    
    def pagos_mes_actual(self):
        pagos_mes_actual = self.get_historial_pagos().filter(fecha__month=timezone.now().month)
        suma = 0
        for pago in pagos_mes_actual:
            suma += pago.monto
        
        return suma
    
    def balance_mes_actual(self):
        return self.cuota_fija_total() + self.cuota_movil_total() - self.pagos_mes_actual()
    

class SocioGrupo(models.Model):
    grupo = models.ForeignKey(GrupoFamiliar,on_delete=models.CASCADE)
    socio = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.socio} de la {self.grupo}"

#pagos de mensualidad y montos fijos/moviles
# class Tarjeta(models.Model):
#     numero = models.CharField(max_length=16)
#     hasta = models.DateField(unique_for_date="1")
#     codigo = models.CharField(max_length=3)
#     usuario = models.CharField(max_length=50)

class Pago(models.Model):
    grupo = models.ForeignKey(GrupoFamiliar, on_delete=models.CASCADE, default=1)
    monto = models.IntegerField()
    fecha = models.DateField(default=timezone.now)
    # aprobado = models.BooleanField(default=False)
    # tarjeta = models.ForeignKey(Tarjeta, on_delete=models.DO_NOTHING, default=1)

    def __str__(self) -> str:
        return f'{self.grupo} por {self.monto} el {self.fecha}'
    

class CambioMensualidadFija(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField()

    def get_comunicado(self):
        return f"Buenos días.\n     Se le comunica a todos los socios que a partir del {self.fecha} la cuota del club pasará a ser de ${self.monto}.\nSepan disculpar las molestias. Muchas gracias por ser parte de nuestra comunidad. \nAtte. la dirección."

    def __str__(self) -> str:
        return f'Cambio a ${self.monto} el {self.fecha}'


#comunicados del club
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    titulo = models.CharField(max_length=50)
    seccion = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    cuerpo = models.CharField(default="")
    fecha = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.seccion}, {self.titulo}, {self.fecha}'