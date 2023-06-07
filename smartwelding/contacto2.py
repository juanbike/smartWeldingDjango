from django import forms
from django.shortcuts import render

class MyForm(forms.Form):
        first_name = forms.CharField(max_length=100, label='First Name')
        last_name = forms.CharField(max_length=100, label='Last Name')
        email = forms.EmailField(label='Email Address')
        message = forms.CharField(widget=forms.Textarea, label='Message')
        
# creamos una función de vista que maneje las solicitudes GET y POST:

def contact(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to the database, send an email, etc.)
            pass
    else:
        form = MyForm()

    return render(request, 'pages/contact.html', {'form': form})

    """En esta función de vista, creamos una instancia del formulario con datos request.POST 
    si el método de solicitud es POST, y sin argumentos si el método de solicitud es GET. Luego verificamos si el formulario es válido y procesamos los datos del formulario en consecuencia.
    """        