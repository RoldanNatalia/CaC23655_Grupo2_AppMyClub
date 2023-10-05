from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=60)
    dni=models.IntegerField
    email=models.EmailField
    direccion=models.CharField(max_length=100)