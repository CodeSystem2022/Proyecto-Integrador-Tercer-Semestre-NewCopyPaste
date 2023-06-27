from django.urls import path
from . import views  # Importo las vistas de myapp

# Defino las urls de mi app base
urlpatterns = [
    path('', views.inicio, name='inicio'),  #  Agrego la url de /
    path('salir/', views.salir, name='salir'), #  Agrego la url de /salir
    path('configuracion/', views.configuracion, name='configuracion'), #  Agrego la url de /login

]
