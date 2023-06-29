from django.shortcuts import redirect, render
#from smartwelding.models import Soldador, Inspector, Materiales, MaterialesEntregados


# Configuracion del modelo en linea para los materiales entregados
#from .forms import FormMateriales, MaterialesFormSet


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from smartwelding.models import Inspector

from .forms import MaterialEntregadoForm, MaterialEntregadoFormSetFactory




# from .contacto import entregaMaterialesForm

# 4- Creando un formset basico: Importamos la clsae formset creada en contacto.py
# from .forms import ItemFormSet

# Creamos el formset a partir del modelo

# formSetmaterialesE = formset_factory(FormMaterialesE, extra=6)



def miplantilla(request):
    titulo = 'Bienvenidos a mi vista'
    contenido = 'Esta es una plantilla en Django'
    return render(request, 'pages/miplantilla.html', {'titulo': titulo, 'contenido': contenido})


class MaterialEntregadoCreateView(CreateView):
    model = Inspector
    template_name = 'pages/material_entregado_form.html'
    form_class = MaterialEntregadoForm
    success_url = reverse_lazy('material_entregado_list')


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = MaterialEntregadoFormSetFactory(
                self.request.POST, instance=self.object
            )
        else:
            data['formset'] = MaterialEntregadoFormSetFactory(instance=self.object)
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))



"""

def miplantilla(request):
    inspectores = Inspector.objects.all()
    soldadores = Soldador.objects.all()
   
    print(inspectores)
    return render(request, 'pages/miplantilla.html', {'inspectores': inspectores, 'soldadores': soldadores})

# Configuracion del modelo en linea para los materiales entregados: Función que recibe las solicitudes Get y Post para agregar materiales


def agregar_materiales_entregados(request, parent_id=None):
    inspectores = Inspector.objects.all()
    soldadores = Soldador.objects.all()
    materiales = Materiales.objects.all()
   
    if parent_id:
        parent = Materiales.objects.get(pk=parent_id)
    else:
        parent = Materiales()

    if request.method == 'POST':
        form = FormMateriales(request.POST, instance=parent)
        formset = MaterialesFormSet(
            request.POST, instance=parent, prefix='children')

        if form.is_valid():
            print("form es valido")
            
        if formset.is_valid():
            print("formset es valido")    
        if form.is_valid() and formset.is_valid():
            #parent = form.save()
            #Crea una instancia de MaterialesEntregados con los datos del formulario
            materiales_entregados = MaterialesEntregados(
                nommbreInspector=form.cleaned_data['nommbreInspector'],
                apellidoInspector=form.cleaned_data['apellidoInspector'],
                nombreSoldador=form.cleaned_data['nombreSoldador'],
                apellidoSoldador=form.cleaned_data['apellidoSoldador'],
                coladaE=form.cleaned_data['coladaE'],
                tipoE=form.cleaned_data['tipoE'],
                sheduleE=form.cleaned_data['sheduleE'],
                tipoExtremoE=form.cleaned_data['tipoExtremoE'],
                tipoMaterialE=form.cleaned_data['tipoMaterialE'],
                materialE=form.cleaned_data[' materialE'],
            )
            materiales_entregados.save()
            formset.save()
           # return redirect('parent_list')
    else:
        form = FormMateriales(instance=parent)
        formset = MaterialesFormSet(instance=parent, prefix='children')
    context = {'form': form, 'formset': formset, 'inspectores': inspectores, 'soldadores': soldadores, 'materiales': materiales}
    return render(request, 'pages/manage_children.html', context)
"""



"""
En esta función de vista, instanciamos el formset con request.POSTdatos si el método de solicitud es POST y sin argumentos si el método de solicitud es GET.
Luego verificamos si el formset es válido y procesamos los datos del formulario en consecuencia.
"""


"""
PASO-4:
La vista espera una solicitud HTTP POST que contenga datos del formulario de entrega de materiales. Si la solicitud es un POST, el código crea 
una instancia de un formulario de entrega de materiales (usando la clase entregaMaterialesForm), y luego verifica si es válido llamando al 
método is_valid() del formulario. Si el formulario es válido, se guarda la instancia mediante el método save(), y la vista redirecciona al 
usuario a la página de materiales entregados.

Si la solicitud no es un POST, se crea una instancia vacía del formulario de entrega de materiales y se muestra al usuario para que pueda 
completarla. En ambos casos, el formulario se pasa al contexto de la plantilla para que pueda ser renderizado en la plantilla 
crear_entregaMateriales.html.
"""


"""
def crear_entregaMateriales(request):
    if request.method == 'POST':
        form = entregaMaterialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materiales_Entregados')
    else:
        form = entregaMaterialesForm()
    return render(request, 'pages/crear_entregaMateriales.html', {'form': form})
"""
