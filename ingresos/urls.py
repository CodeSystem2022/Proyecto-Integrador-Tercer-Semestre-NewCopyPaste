from django.urls import path # Importo path
from . import views  # Importo las vistas de mi app ingresos


# Defino las urls de mi app ingresos
urlpatterns = [
    path('', views.crearIngreso, name='ingresoVehiculos'), # Agrego la url de /vehiculos/ingresos
    path('listado/', views.listado, name='ListadoVehiculos'), # Agrego la url de /vehiculos/ingresos/listado
    path('eliminar/<int:id>', views.eliminar, name='EliminarVehiculos'), # Agrego la url de /vehiculos/ingresos/eliminar
]
