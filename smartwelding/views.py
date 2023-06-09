from django.shortcuts import redirect, render
from django.http import HttpResponse
from smartwelding.models import Soldador, Inspector
from django.forms import formset_factory
from .forms import FormMaterialesE
from .contacto import entregaMaterialesForm

#4- Creando un formset basico: Importamos la clsae formset creada en contacto.py
#from .forms import ItemFormSet

#Creamos el formset a partir del modelo

formSetmaterialesE = formset_factory(FormMaterialesE, extra=6)




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

#5- viene de contacto.py cree una función de vista que maneje las solicitudes GET y POST
"""
def items(request):
    if request.method == 'POST':
        formset = ItemFormSet(request.POST, prefix='items')
        if formset.is_valid():
            # Process the form data (e.g., save to the database, send an email, etc.)
            pass
    else:
        formset = ItemFormSet(prefix='items')

    return render(request, 'pages/items.html', {'formset': formset})
"""    

"""
En esta función de vista, instanciamos el formset con request.POSTdatos si el método de solicitud es POST y sin argumentos si el método de solicitud es GET.
Luego verificamos si el formset es válido y procesamos los datos del formulario en consecuencia.
"""    

#6- cree la plantilla vaya a templates/pages/items.html

def crear_entregaMateriales(request):
    if request.method == 'POST':
        form = entregaMaterialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materiales_Entregados')
    else:
        form = entregaMaterialesForm()
    return render(request, 'pages/crear_entregaMateriales.html', {'form': form})