from django import forms
from django.forms import inlineformset_factory
from .models import (Materiales,  MaterialesEntregados, Inspector, Soldador)






# ------------- Defnimos los formularios Padre - hijo ------------------------

# ----- FORMULARIO PADRE O  FORM---------------
"""
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


#MaterialesFormSet = inlineformset_factory(Materiales, MaterialesEntregados, form= FormMaterialesEntegados, extra=4)    
MaterialesFormSet = inlineformset_factory(Inspector, MaterialesEntregados, form= FormMaterialesEntegados, extra=4)    


"""

class MaterialEntregadoForm(forms.ModelForm):
    class Meta:
        model = MaterialesEntregados
        fields = ['tipoE', 'tipoExtremoE', 'coladaE', 'sheduleE', 'tipoMaterialE', 'materialE']

class MaterialEntregadoFormSet(forms.BaseInlineFormSet):
    inspector = forms.ModelChoiceField(queryset=Inspector.objects.all())
    soldador = forms.ModelChoiceField(queryset=Soldador.objects.all())


MaterialEntregadoFormSetFactory = inlineformset_factory(
    Inspector, MaterialesEntregados, form=MaterialEntregadoForm, 
    formset=MaterialEntregadoFormSet, extra=1, can_delete=True
)