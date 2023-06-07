from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from requests import request
from django.core.exceptions import ValidationError
from .models import Linea

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
