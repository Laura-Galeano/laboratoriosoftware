from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, 'Home.html')

#{% load crispy_forms_tags %}
def crearAutor(request):
    if request.method == 'POST':
        autor_form = autorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')
    else:
        autor_form = autorForm()
    return render(request, 'registration/Registrarse.html',{'autor_form':autor_form})


def listarAutor(request):
    autores = autor.objects.all() #autor se refiere al modelo
    return render(request, 'libro/listarAutor.html', {'autores':autores})

def editarAutor(request,id_autor):
    autor_form = None
    error = None
    try:
        Autor = autor.objects.get(id_autor = id_autor)
        tipo_autor = Autor.tipo_autor
        if request.method == 'GET':
            autor_form = autorForm(instance = Autor)
        else:
            autor_form = autorForm(request.POST, instance=Autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('/libro/editarAutor/'+str(id_autor))
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'editarperfil.html', {'autor_form':autor_form, 'error':error, 'id_autor':id_autor, 'tipo_autor':tipo_autor})

def login(request):
    if request.method == 'POST':
        print(request.POST['usuario'])
        data = autor.objects.get(usuario=request.POST['usuario'])
        if data.contrasena == request.POST['contrasena']:
            id = str(data.id_autor)
            return redirect('/libro/editarAutor/'+id)
        else:
            print("El autor no existe")
            return redirect('/login')
    return render(request,"registration/login.html")

def crearTarjeta(request):
    tarjeta_form = None
    error = None
    if request.method == 'POST':
        tarjeta_form = tarjetaForm(request.POST)
        if tarjeta_form.is_valid():
            tarjeta_form.save()
            return redirect('/')
    else:
        tarjeta_form = tarjetaForm()
    return render(request, 'libro/crearTarjeta.html', {'tarjeta_form':tarjeta_form, 'error':error})

def editarTarjeta(request, id_tarjeta):
    tarjeta_form = None
    error = None
    try:
        Tarjeta = tarjeta.objects.get(id_tarjeta = id_tarjeta)
        if request.method == 'GET':
            tarjeta_form = tarjetaForm(instance = Tarjeta)
        else:
            tarjeta_form = tarjetaForm(request.POST, instance=Tarjeta)
            if tarjeta_form.is_valid():
                tarjeta_form.save()
            return redirect('/')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crearTarjeta.html', {'tarjeta_form':tarjeta_form, 'error':error})

def adminLibros(request):
    libros = libro.objects.all() #libro se refiere al modelo
    return render(request, 'libro/adminLibros.html', {'libros':libros})

def crearLibro(request):
    #libro_form = None
    error = None
    if request.method == 'POST':
        libro_form = libroForm(request.POST)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('/libro/adminLibros')
    else:
        libro_form = libroForm()
    return render(request, 'libro/crearLibro.html', {'libro_form':libro_form, 'error':error})

def editarLibro(request,issn):
    libro_form = None
    error = None
    try:
        Libro = libro.objects.get(issn = issn)
        print(issn)
        if request.method == 'GET':
            libro_form = libroForm(instance = Libro)
        else:
            libro_form = libroForm(request.POST, instance=Libro)
            if libro_form.is_valid():
                libro_form.save()
            return redirect('/libro/adminLibros')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crearLibro.html', {'libro_form':libro_form, 'error':error})

def eliminarLibro(request,issn):
    Libro = libro.objects.get(issn = issn)
    Libro.delete()
    return redirect('/libro/adminLibros')

def adminTarjeta(request,id_autor):
    tarjetas = tarjeta.objects.filter(id_autor = id_autor) #libro se refiere al modelo
    return render(request, 'libro/adminTarjeta.html', {'tarjetas':tarjetas, 'id_autor':id_autor})

def eliminarTarjeta(request,id_autor,id_tarjeta):
    Tarjeta = tarjeta.objects.get(id_tarjeta = id_tarjeta)
    Tarjeta.delete()
    return redirect('/libro/adminTarjeta/'+str(id_autor))

def listarLibros(request,id_autor):
    libros = libro.objects.all() #libro se refiere al modelo
    return render(request, 'libro/listarLibros.html', {'libros':libros, 'id_autor':id_autor})

def comprarLibro(request,id_autor,issn):
    try:
        compra_form = compraForm()
        compra_form.id_autor = str(id_autor)
        compra_form.issn = str(issn)
        if request.method == "POST":
            if compra_form.is_valid():
                compra_form.save()
                return redirect('/libro/editarAutor/'+str(id_autor))
    except ObjectDoesNotExist as e:
        return HttpResponse("Hay un error")
    return HttpResponse("Hay un error")
