from django.shortcuts import render # importar render para renderizar las paginas
from ingresos.models import Ingreso # importar el modelo Ingreso para obtener los ingresos
from django.utils import timezone # importar timezone para obtener la hora actual
from datetime import datetime # importar datetime para obtener la hora actual
from .models import Comprobante # importar el modelo Comprobante para crear un comprobante de pago
from base.models import Configuracion # importar el modelo Configuracion para obtener la cantidad de cocheras


def egresoVehiculos(request): # funcion que se encarga de mostrar los vehiculos que estan en el estacionamiento
    ingresos = Ingreso.objects.all()  # obtener todos los ingresos

    # agregar el tiempo actual a cada ingreso para calcular el tiempo de estadia en el estacionamiento
    for ingreso in ingresos: # recorrer todos los ingresos
        ingreso.tiempo = timezone.now() # agregar el tiempo actual a cada ingreso 

    # calcular el tiempo de estadia en el estacionamiento y formatearlo a horas y minutos
    for ingreso in ingresos: # recorrer todos los ingresos
        tiempo_actual = timezone.now() # obtener el tiempo actual
        tiempo_transcurrido = (tiempo_actual - ingreso.fechaIngreso).total_seconds() / 3600 # calcular el tiempo transcurrido en el estacionamiento
        ingreso.tiempo = round(tiempo_transcurrido, 2)  # redondear el tiempo transcurrido a 2 decimales

    return render(request, 'vehiculos/egresos.html', {'ingresos': ingresos}) # renderizar la pagina de egresos y pasarle los ingresos


def cobrar(request, id): # funcion que se encarga de cobrar el estacionamiento
    ingreso = Ingreso.objects.get(pk=id) # obtener el ingreso con el id de cochera

    tiempo_actual = timezone.now() # obtener el tiempo actual
    tiempo_transcurrido = (tiempo_actual - ingreso.fechaIngreso).total_seconds() / 3600 # calcular el tiempo transcurrido en el estacionamiento
    ingreso.estadia = round(tiempo_transcurrido, 2) # redondear el tiempo transcurrido a 2 decimales

    precio = Configuracion.objects.get(titulo='Precio').valor
    precio = float(precio)
   

    # calcular el costo de la estadia en el estacionamiento si vale 100 pesos la hora
    ingreso.costo = round(ingreso.estadia * precio, 2) # redondear el costo a 2 decimales
    ingreso.fechaSalida = datetime.now() # agregar la fecha de salida al ingreso

    return render(request, 'vehiculos/cobrar.html', {'ingreso': ingreso}) # renderizar la pagina de cobrar y pasarle el ingreso


def comprobante(request): # funcion que se encarga de crear un comprobante de pago



    if request.method == 'POST': # si el metodo es POST
        print(request.POST)
        Comprobante.objects.create( 
             nombre=request.POST['nombre'], apellido=request.POST['apellido'], telefono=request.POST['telefono'], fechaIngreso=request.POST['fechaIngreso'], fechaSalida=request.POST['fechaSalida'], estadia=request.POST['estadia'], costo=request.POST['costo'], cochera=request.POST['idCochera'], tipo=request.POST['tipo'], dominio=request.POST['dominio']) # crear un comprobante de pago con los datos del formulario
        #obtener el id del comprobante creado
        comprobante = Comprobante.objects.latest('id') # obtener el ultimo comprobante creado
        
        #obtener el ingreso con el id de cochera
        DatosComprobante = Comprobante.objects.get(pk=comprobante.id) # obtener el comprobante con el id de cochera

        #eliminar el ingreso con el idIngreso 
        Ingreso.objects.filter(id=request.POST['idIngreso']).delete()
        




        return render(request, 'vehiculos/comprobante.html', {'DatosComprobante': DatosComprobante})
    else:
        print(request.POST)
        return render(request, 'vehiculos/comprobante.html')
    

def listarComprobante(request): # funcion que se encarga de listar los comprobantes de pago
    comprobantes = Comprobante.objects.all() # obtener todos los comprobantes de pago

    return render(request, 'vehiculos/listarComprobante.html', {'comprobantes': comprobantes}) # renderizar la pagina de listar comprobantes y pasarle los comprobantes