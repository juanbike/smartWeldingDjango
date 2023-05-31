from django.db import models

# Create your models here.
class Soldadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    altura = models.FloatField()
    creado = models.DateTimeField(auto_now=True)