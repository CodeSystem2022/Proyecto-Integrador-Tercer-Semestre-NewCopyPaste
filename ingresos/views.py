from django.shortcuts import render, redirect
from .models import Ingreso
from .forms import CrearNuevoIngresovehiculos

# Create your views here.


def ingreso(request):
    return render(request, 'vehiculos/ingresos.html')


def listado(request):
    ingresos = Ingreso.objects.all()
    return render(request, 'vehiculos/listado.html', {'listaIngresos': ingresos})


def crearIngreso(request):
    if request.method == 'GET':
        print(request.GET)
        # Agrego el formulario
        return render(request, 'vehiculos/ingresos.html', {'form': CrearNuevoIngresovehiculos()})
    else:
        print(request.POST)
        Ingreso.objects.create(
            tipo=request.POST['tipo'], dominio=request.POST['dominio'],  observaciones=request.POST['observaciones'],  idCochera=request.POST['idCochera'])
        return redirect('ListadoVehiculos')


def eliminar(request, id):
    Ingreso.objects.filter(id=id).delete()
    return redirect('ListadoVehiculos')
