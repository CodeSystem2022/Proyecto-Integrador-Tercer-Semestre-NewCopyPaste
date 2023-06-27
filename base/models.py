from django.db import models

# Create your models here.

class Configuracion(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo + ' - ' + self.descripcion + ' -  ' + self.valor
