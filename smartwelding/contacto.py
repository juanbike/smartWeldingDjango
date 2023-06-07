from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from requests import request


class ContactoForm(forms.Form):
    sunombre = forms.CharField(max_length=100, label='Su nombre')
    email = forms.EmailField(required=False, label='Su correo')


subject = forms.CharField(max_length=100)
message = forms.CharField(widget=forms.Textarea)


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
