from django.db import models

# Create your models here.

class Ingreso(models.Model):
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    dominio = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    # hora = models.TimeField()
    observaciones = models.TextField(blank=True)
    idCochera = models.IntegerField(default=0)
    


    def __str__(self):
        return self.dominio + " - " + self.tipo + " - " + str(self.fechaIngreso) + " - " + str(self.idCochera) # Retorno el dominio, tipo, fecha,  estado y cochera

