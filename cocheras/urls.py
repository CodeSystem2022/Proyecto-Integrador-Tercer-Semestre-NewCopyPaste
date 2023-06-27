#URL configuration for cocheras project.

from django.contrib import admin
from django.urls import path, include  # Agrego include


# Defino las urls de mi proyecto cocheras
urlpatterns = [
    path('', include('base.urls')), # Agrego la url de /
    path('inicio/', include('base.urls')),  # Agrego la url de /inicio
    path('admin/', admin.site.urls), # Agrego la url de /admin
    path('vehiculos/ingresos/', include('ingresos.urls')), # Agrego la url de /vehiculos/ingresos
    path('vehiculos/salidas/', include('egresos.urls')), # Agrego la url de /vehiculos/egresos
]
