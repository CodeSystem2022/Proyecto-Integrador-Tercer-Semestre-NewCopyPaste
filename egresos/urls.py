from django.urls import path
from . import views  # Importo las vistas de mi app ingresos




# Defino las urls de mi app ingresos
urlpatterns = [
    path('', views.egresoVehiculos, name='egresosVehiculos'),
    #agregar url cobrar/id para que me lleve a la vista cobrar
    path('cobrar/<int:id>', views.cobrar, name='cobrar'),
    path('comprobante/', views.comprobante, name='comprobante'),
    path('listar/comprobante/', views.listarComprobante, name='listarComprobante'),
]
