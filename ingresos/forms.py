from django import forms
from base.models import Configuracion

totalCocheras = Configuracion.objects.get(titulo='Cocheras').valor

class CrearNuevoIngresovehiculos(forms.Form):
    
    tipo = forms.CharField(max_length=200, label="Tipo de Vehiculo", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ej: Auto, Moto, Camioneta'}))
    dominio = forms.CharField(max_length=200, label="Dominio", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ej: AA025KE'}))
    # fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ej: 2020-12-31'}))
    # hora = forms.TimeField(label="Hora", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ej: 12:00'}))
    observaciones = forms.CharField(label="Observaciones", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    idCochera = forms.ChoiceField(label="Cochera", choices=[(x, x) for x in range(1, int(totalCocheras)+1)], widget=forms.Select(attrs={'class' : 'form-control'}))


    


    
