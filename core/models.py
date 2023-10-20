from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=60)
    dni=models.CharField(max_length=8)
    email=models.EmailField(max_length=100,default="to1@example.com")
    direccion=models.CharField(max_length=100,default="Domicilio..")

    
