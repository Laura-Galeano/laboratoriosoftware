from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = autorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')
    else:
        autor_form = autorForm()
    return render(request, 'libro/crearAutor.html',{'autor_form':autor_form})


def listarAutor(request):
    autores = autor.objects.all() #autor se refiere al modelo
    return render(request, 'libro/listarAutor.html', {'autores':autores})

def editarAutor(request,id_autor):
    autor_form = None
    error = None
    try:
        Autor = autor.objects.get(id_autor = id_autor)
        if request.method == 'GET':
            autor_form = autorForm(instance = Autor)
            print(autor_form)
        else:
            autor_form = autorForm(request.POST, instance=Autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('/')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crearAutor.html', {'autor_form':autor_form, 'error':error})
