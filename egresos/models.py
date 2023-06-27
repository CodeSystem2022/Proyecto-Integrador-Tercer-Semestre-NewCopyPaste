from django.db import models

# Create your models here.

class Comprobante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fechaIngreso = models.CharField(max_length=50)
    fechaSalida = models.CharField(max_length=50)
    estadia = models.FloatField()
    costo = models.FloatField()
    cochera = models.IntegerField()
    tipo = models.CharField(max_length=50)
    dominio = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.dominio + " " + self.tipo  + " " + str(self.costo) 
