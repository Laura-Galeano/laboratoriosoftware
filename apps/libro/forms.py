from django import forms
from .models import *

class autorForm(forms.ModelForm):
    class Meta:
        model = autor
        #fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        fields = '__all__'

class autorAuthenticacion(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['usuario', 'contrasena']

class tarjetaForm(forms.ModelForm):
    class Meta:
        model = tarjeta
        fields = '__all__'

class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = '__all__'
