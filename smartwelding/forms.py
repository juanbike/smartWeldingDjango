from django import forms
from django.forms import inlineformset_factory
from .models import Materiales,  MaterialesEntregados, Inspector, Soldador






# ------------- Defnimos los formularios Padre - hijo ------------------------

# Formulario Padre

class FormMateriales(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['nombreI', 'apellidoI'],
    class Meta:    
        model = Soldador
        fields = ['nombre', 'apellido']
        opciones = forms.ModelChoiceField(queryset=Inspector.objects.all())
# Formulario Hijo
class FormMaterialesEntegados(forms.ModelForm):
    class Meta:
        model = MaterialesEntregados
        fields =['tipoE', 'tipoExtremoE', 'coladaE', 'sheduleE', 'tipoMaterialE', 'materialE' ]


MateialesFormSet = inlineformset_factory(Materiales, MaterialesEntregados, form= FormMaterialesEntegados, extra=4)    


