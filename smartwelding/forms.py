from django import forms
from django.forms import inlineformset_factory
from .models import (Materiales,  MaterialesEntregados, Inspector, Soldador)






# ------------- Defnimos los formularios Padre - hijo ------------------------

# ----- FORMULARIO PADRE O  FORM---------------

class FormMateriales(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['nombre', 'apellido'],
    class Meta:    
        model = Soldador
        fields = ['nombre', 'apellido']
       


# ------ FORMULARIO HIJO O FORMSET ------------
class FormMaterialesEntegados(forms.ModelForm):
    class Meta:
        model = MaterialesEntregados
        fields =['tipoE', 'tipoExtremoE', 'coladaE', 'sheduleE', 'tipoMaterialE', 'materialE' ]


MaterialesFormSet = inlineformset_factory(Materiales, MaterialesEntregados, form= FormMaterialesEntegados, extra=4)    


