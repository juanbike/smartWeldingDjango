from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from requests import request
from django.core.exceptions import ValidationError
from .models import Linea

#1-Creando un formset basico: importar los modulos necesarios
from django import forms
from django.forms import formset_factory

#1- Gestión de conjuntos de formularios en línea en Django: Importar los módulos necesarios:
from django.forms import inlineformset_factory
from .models import Inspector, MaterialesEntregados




# creamos la clase ContactoForm tiene los metodos y propiedades para el formulario de contacto


class ContactoForm(forms.Form):
    sunombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ingese su nombre', 'maxlenght': '12'}))
    email = forms.EmailField(required=False, label='Su correo')
    subject = forms.CharField(max_length=100)
    linea = forms.ModelChoiceField(queryset=Linea.objects.all(), empty_label='Seleccione una linea') 
    mensaje = forms.CharField(widget=forms.Textarea ,label='Mensaje', min_length=10)


# Creamos una funcion para manejar las solicitudes get y post desde el cliente
def contacto(request):
    submitted = False
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contacto?submitted=True')
    else:
        form = ContactoForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'pages/contacto.html',
                  {'form': form, 'submitted': submitted}
                  )


def clean_mensaje(self):
    mensaje = self.cleaned_data['mensaje']
    if len(mensaje) < 10:
        raise forms.ValidationError(
            "El mensaje debe tener al menos 10 caracteres.")
    return mensaje


#Creando un formset basico
#2- Defina una clase de formulario:
class ItemForm(forms.Form):
    name = forms.CharField(max_length=100, label='Item Name')
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    price = forms.DecimalField(min_value=0, decimal_places=2, label='Price')

#3-Crea una clase de formset usando formset_factory:    
ItemFormSet = formset_factory(ItemForm, extra=3)
"""
La función formset_factory crea una clase de conjunto de formularios para el formulario especificado. El parámetro extra indica el número de formularios
 vacíos que se mostrarán inicialmente, que se establece en 1 en este ejemplo.
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



#1- Gestión de conjuntos de formularios en línea en Django:Defina los formularios del modelo padre e hijo:

class ParentModelForm(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['nombre', 'apellido', 'telefono', 'telefono2']

class ChildModelForm(forms.ModelForm):
    class Meta:
        model = MaterialesEntregados
        fields = ['tipoE', 'sheduleE', 'tipoExtremoE','materialE' ]
 
 
 #2- Cree una clase de formset en línea usando inlineformset_factory:       
class  ChildModelFormSet : inlineformset_factory(Inspector, MaterialesEntregados, form=ChildModelForm, extra=1, can_delete=True)



#4- Utilice el formset en línea en una vista de Django:

def manage_children(request, parent_id=None):
    if parent_id:
        parent = Inspector.objects.get(pk=parent_id)
    else:
        parent = Inspector()

    if request.method == 'POST':
        form = ParentModelForm(request.POST, instance=parent)
        formset = ChildModelFormSet(request.POST, instance=parent, prefix='children')

        if form.is_valid() and formset.is_valid():
            parent = form.save()
            formset.save()
            return redirect('parent_list')
    else:
        form = ParentModelForm(instance=parent)
        formset = ChildModelFormSet(instance=parent, prefix='children')

    return render(request, 'pages/manage_children.html', {'form': form, 'formset': formset})


"""
En esta función de vista, instanciamos el formulario principal y el conjunto de formularios en línea con datos request.
POST si el método de solicitud es POST, y sin argumentos si el método de solicitud es GET. Luego verificamos si tanto el formulario 
como el conjunto de formularios son válidos y guardamos las instancias en consecuencia.
"""