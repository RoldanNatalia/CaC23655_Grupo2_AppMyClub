from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=60)
    dni=models.CharField(max_length=8)
    email=models.EmailField(max_length=100,default="to1@example.com")
    direccion=models.CharField(max_length=100,default="Domicilio..")

    class Meta():
        abstract = "true"
    
    def clean_dni(self):
        if not self.cleaned_data['dni'].isnumeric():
            raise ValidationError("El dni debe ser numerico")

        return self.cleaned_data['dni']
    
class Actividad(models.Model):
    nombre = models.CharField(max_length=30)

class Socio(Persona):
    numero = models.CharField(max_length=5)

class Profesor(Persona):
    actividad = models.ForeignKey(Actividad,on_delete=models.CASCADE)

class Predio(models.Model):
    nombre = models.CharField(max_length=40, unique=True)

class Dia(models.Model):
    dia = models.CharField(max_length=9, unique=True)

    def clean_dia(self):
        if not self.cleaned_data['dia'] in ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]:
            raise ValidationError("Dia no pertenece al calendario") 

        return self.cleaned_data['dia']

class Curso(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Socio, through="Inscripcion")
    dias = models.ManyToManyField(Dia, through="DiaCurso")
    desde = models.FloatField()
    hasta = models.FloatField()
    predio = models.ForeignKey(Predio, on_delete=models.DO_NOTHING)
    mensualidad = models.IntegerField()

    def clean_horario(self):
        if not(0 < self.cleaned_data['desde'] < 24 and 0 < self.cleaned_data['hasta'] < 24 ):
            raise ValidationError("Fechas incorrectas no cumplen formato de 24hs")
        if not(self.cleaned_data['desde'] < self.cleaned_data['hasta']):
            raise ValidationError("El inicio debe ser menor que el final de la clase")

        return (self.cleaned_data['desde'],self.cleaned_data['hasta'])
    
    def clean_mensualidad(self):
        if self.cleaned_data['mensualidad'] < 0:
            raise ValidationError("La mensualidad no puede ser negativa")

        return self.cleaned_data['mensualidad']

class DiaCurso(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)

class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha = models.DateField()

class Reserva(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha = models.DateField()
    desde = models.FloatField()
    hasta = models.FloatField()

    def calcular_dia(self):
        dia = self.fecha.day
        mes = self.fecha.month
        anio = self.fecha.year

        codigo_mes = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

        anio -= mes < 3

        dia_codigo = (anio + anio / 4 - anio / 100 + anio / 400 + codigo_mes[mes - 1] + dia) % 7

        lista_dias = ['sabado','domingo','lunes','martes','miercoles','jueves','viernes']

        return lista_dias[dia_codigo]

    def clean_horario(self):
        if not(0 < self.cleaned_data['desde'] < 24 and 0 < self.cleaned_data['hasta'] < 24 ):
            raise ValidationError("Fechas incorrectas no cumplen formato de 24hs")
        if not(self.cleaned_data['desde'] < self.cleaned_data['hasta']):
            raise ValidationError("El inicio debe ser menor que el final de la clase")

        return (self.cleaned_data['desde'],self.cleaned_data['hasta'])

    def clean_fecha(self):
        cursos = Curso.objects.all()
        
        for curso in cursos:
            if self.predio == curso.predio and ((curso.desde < self.desde < curso.hasta) or (curso.desde < self.hasta < curso.hasta)):
                if(self.calcular_dia() in curso.dias):
                    raise ValidationError('Ya existe una actividad en el predio y horario asignado')
        


    