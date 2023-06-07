from django.shortcuts import render
from django.http import HttpResponse
from smartwelding.models import Soldador, Inspector


""""
def miplantilla(request):
    titulo = 'Bienvenidos a mi vista'
    contenido = 'Esta es una plantilla en Django'
    return render(request, 'pages/miplantilla.html', {'titulo': titulo, 'contenido': contenido})
"""


def miplantilla(request):
    inspectores = Inspector.objects.all()
    soldadores = Soldador.objects.all()
    print(inspectores)
    return render(request, 'pages/miplantilla.html', {'inspectores': inspectores, 'soldadores': soldadores })

