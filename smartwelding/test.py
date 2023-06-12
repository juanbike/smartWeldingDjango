from django.test import TestCase
from .models import Inspector, Soldador, Proyecto, MaterialesEntregados

class MaterialesEntregadosTestCase(TestCase):
    def setUp(self):
        # Creamos algunos registros de prueba para los modelos
        self.inspector1 = Inspector.objects.create(nombre='Juan')
        self.inspector2 = Inspector.objects.create(nombre='Pedro')
        self.soldador1 = Soldador.objects.create(nombre='Manuel')
        self.soldador2 = Soldador.objects.create(nombre='Luis')
        self.proyecto1 = Proyecto.objects.create(nombre='Construcción de edificio')
        self.proyecto2 = Proyecto.objects.create(nombre='Construcción de puente')

    def test_materiales_entregados(self):
        # Creamos un registro de materiales entregados
        materiales_entregados = MaterialesEntregados.objects.create(
            inspector=self.inspector1,
            soldador=self.soldador1,
            proyecto=self.proyecto1,
            cantidad_entregada=100,
            fecha_entrega='2022-06-12'
        )

        # Verificamos que el objeto MaterialesEntregados se haya creado correctamente
        self.assertEqual(materiales_entregados.inspector, self.inspector1)
        self.assertEqual(materiales_entregados.soldador, self.soldador1)
        self.assertEqual(materiales_entregados.proyecto, self.proyecto1)
        self.assertEqual(materiales_entregados.cantidad_entregada, 100)
        self.assertEqual(materiales_entregados.fecha_entrega, '2022-06-12')