from django.contrib import admin
from .models import Ingreso

class IngresoAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaIngreso',) # Hago que el campo fecha sea de solo lectura
    #list_display = ('fecha',) # Muestro los campos fecha, dominio, tipo, cochera
    #quiero ver y editar fecha
    #list_display = ('fecha', 'dominio', 'tipo', 'idCochera', 'observaciones') # Muestro los campos fecha, dominio, tipo, cochera

# Registrando el modelo Ingreso en el admin de django
admin.site.register(Ingreso, IngresoAdmin)

