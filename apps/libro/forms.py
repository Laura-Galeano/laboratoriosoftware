from django import forms
from .models import *

class autorForm(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        
