from django.shortcuts import render
from django.http import HttpResponse

def miplantilla(request):
    titulo = 'Bienvenidos a mi vista'
    contenido = 'Esta es una plantilla en Django'
    return render(request, 'pages/miplantilla.html', {'titulo': titulo, 'contenido': contenido})