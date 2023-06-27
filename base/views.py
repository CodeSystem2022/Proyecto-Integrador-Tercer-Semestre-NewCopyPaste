from django.shortcuts import render
from .models import Configuracion
# Create your views here.



def inicio(request): # Defino la vista de inicio
    title = "UTN SAN RAFAEL"
    title2 = "Tecnicatura Universitaria en Programación"
    return render(request, 'index.html', {'title': title, 'title2': title2})


def salir(request): # Defino la vista de salir
    return render(request, 'salir.html')

def configuracion(request): # Defino la vista de configuracion
    configuraciones = Configuracion.objects.all()
    return render(request, 'configuracion.html', {'listaConfiguraciones': configuraciones})