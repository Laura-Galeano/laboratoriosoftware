from django.urls import path, include
from .views import *

urlpatterns = [
    path('crearAutor/', crearAutor, name='crearAutor'),
    path('listarAutor/', listarAutor, name='listarAutor'),
    path('editarAutor/<int:id_autor>', editarAutor, name='editarAutor'),
    path('crearTarjeta', crearTarjeta, name='crearTarjeta'),
    path('editarTarjeta/<int:id_tarjeta>', editarTarjeta, name="editarTarjeta"),
    path('adminTarjeta/<int:id_autor>', adminTarjeta, name='adminTarjeta'),
    path('adminLibros/', adminLibros, name='adminLibros'),
    path('crearLibro/', crearLibro, name='crearLibro'),
    path('editarLibro/<int:issn>', editarLibro, name='editarLibro'),
    path('listarLibros/<int:id_autor>', listarLibros, name='listarLibros'),
    path('comprarLibro/<int:id_autor>/<int:issn>', comprarLibro, name='comprarLibro'),
]
