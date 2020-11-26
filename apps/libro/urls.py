from django.urls import path, include
from .views import *

urlpatterns = [
    path('crearAutor/', crearAutor, name='crearAutor'),
    path('listarAutor/', listarAutor, name='listarAutor'),
    path('editarAutor/<int:id_autor>', editarAutor, name='editarAutor'),
    path('crearTarjeta', crearTarjeta, name='crearTarjeta'),
    path('editarTarjeta/<int:id_tarjeta>', editarTarjeta, name="editarTarjeta"),
    path('adminLibros/', adminLibros, name='adminLibros'),
    path('crearLibro/', crearLibro, name='crearLibro'),
    path('editarLibro/<int:issn>', editarLibro, name='editarLibro'),
]
