from django.urls import path, include
from .views import *

urlpatterns = [
    path('crearAutor/', crearAutor, name='crearAutor'),
    path('listarAutor/', listarAutor, name='listarAutor'),
    path('editarAutor/<int:id_autor>', editarAutor, name='editarAutor'),
]
