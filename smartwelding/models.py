from django.db import models
from django.contrib import admin
# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(
        max_length=25, default='Normal', null=False, blank=False)
    telefono = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.telefono}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.telefono}"


class Soldador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    altura = models.FloatField()
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.telefono}"


class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    contacto = models.CharField(max_length=80)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.telefono}"


class Linea(models.Model):
    linea = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.linea}"


class Especificacion(models.Model):
    especificacion = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.especificacion}"


class Materiales(models.Model):
    tipo = models.CharField(max_length=40)
    colada = models.CharField(
        max_length=10, default='00000000', null=False, blank=False)
    shedule = models.CharField(max_length=4)
    tipoExtremo = models.CharField(max_length=15)
    tipoMaterial = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo} {self.tipoMaterial}"


class Diametros(models.Model):
    nominal = models.CharField(max_length=8)
    nominal1 = models.FloatField()
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nominal} {self.nominal1}"


class PulgadasDiametrales(models.Model):
    factorPulgadasDiametrales = models.FloatField()
    pulgadasDiametrales = models.FloatField()
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.factorPulgadasDiametrales} {self.pulgadasDiametrales}"


class MaterialesConsumidos(models.Model):
    coladaC = models.CharField(
        max_length=10, default='00000000', null=False, blank=False)
    tipoC = models.CharField(max_length=40)
    sheduleC = models.CharField(max_length=4)
    tipoExtremoC = models.CharField(max_length=15)
    tipoMaterialC = models.CharField(max_length=30)
    materialC = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.tipoc} {self.shedule} {self.tipoEstremoC} {self.tipoMaterialc} {self.materialC}"


class Inspector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.telefono}"





class MaterialesEntregados(models.Model):
    nombreInspector = models.CharField(max_length=50, default='', null=False, blank=False)
    apellidoInspector = models.CharField(max_length=50, default='', null=False, blank=False)
    nombreSoldador = models.CharField(max_length=50, default='', null=False, blank=False)
    apellidoSoldador = models.CharField(max_length=50, default='', null=False, blank=False)
    nombreProyecto = models.CharField(50, default='', null=False, blank=False)
    coladaE = models.CharField(
        max_length=10, default='00000000', null=False, blank=False)
    tipoE = models.CharField(max_length=40)
    sheduleE = models.CharField(max_length=4)
    tipoExtremoE = models.CharField(max_length=15)
    tipoMaterialE = models.CharField(max_length=30)
    materialE = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)
    #Relacionamos MaterialesEntregados con inspector: Un inspector tiene uno o muchos materiales entregados a los soldadores
    inspector = models.ForeignKey(Inspector, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.tipoE} {self.tipoMaterialE}"


class junta(models.Model):
    tipoJunta = models.CharField(max_length=20)
    linea = models.CharField(max_length=100)
    especificacion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=40)
    shedule = models.CharField(max_length=4)
    tipoExtremo = models.CharField(max_length=15)
    tipoMaterial = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    nominal = models.CharField(max_length=4)
    nominal1 = models.FloatField()
    factorPulgadasDiametrales = models.FloatField()
    pulgadasDiametrales = models.FloatField()
    pulgadasContabilizadas = models.IntegerField()
    creado = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.tipoJunta} {self.Material}"


class juntaAprobada(models.Model):
    linea = models.CharField(
        max_length=100, default='Falta la linea', null=False, blank=False)
    especificacion = models.CharField(max_length=30,  null=False, blank=False)
    tipo = models.CharField(max_length=40,  null=False, blank=False)
    shedule = models.CharField(max_length=4,  null=False, blank=False)
    tipoExtremo = models.CharField(max_length=15,  null=False, blank=False)
    tipoMaterial = models.CharField(max_length=30,  null=False, blank=False)
    material = models.CharField(max_length=30,  null=False, blank=False)
    nominal = models.CharField(max_length=4,  null=False, blank=False)
    nominal1 = models.FloatField(null=False, blank=False)
    factorPulgadasDiametrales = models.FloatField(null=False, blank=False)
    pulgadasDiametrales = models.FloatField(null=False, blank=False)
    pulgadasContabilizadas = models.IntegerField(null=False, blank=False)
    creado = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.linea} {self.creado}"


class juntaRechazada(models.Model):
    linea = models.CharField(
        max_length=100, default='Falta la linea', null=False, blank=False)
    especificacion = models.CharField(max_length=30,  null=False, blank=False)
    tipo = models.CharField(max_length=40,  null=False, blank=False)
    shedule = models.CharField(max_length=4,  null=False, blank=False)
    tipoExtremo = models.CharField(max_length=15,  null=False, blank=False)
    tipoMaterial = models.CharField(max_length=30,  null=False, blank=False)
    material = models.CharField(max_length=30,  null=False, blank=False)
    nominal = models.CharField(max_length=4,  null=False, blank=False)
    nominal1 = models.FloatField(null=False, blank=False)
    factorPulgadasDiametrales = models.FloatField(null=False, blank=False)
    pulgadasDiametrales = models.FloatField(null=False, blank=False)
    pulgadasContabilizadas = models.IntegerField(null=False, blank=False)
    creado = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.linea} {self.creado}"


class PruebaHidrostatica(models.Model):
    nombreInspector = models.CharField(25)
    apellidoInspector = models.CharField(25)
    fecha = models.DateField()
    nombreObra = models.CharField(30)
    lugarObra = models.CharField(30)
    material = models.CharField(25)
    tipo = models.CharField(30)
    clase = models.CharField(30)
    diametro = models.CharField(30)
    # NO ACEPTA VALORES NULOS NI VACIOS
    tramoKm = models.IntegerField(default=1, null=False, blank=False)
    alKm = models.IntegerField(default=1, null=False, blank=False)
    longitud = models.IntegerField(default=1, null=False, blank=False)
    uniones = models.IntegerField(default=1, null=False, blank=False)
    temperaturaAmbiente = models.FloatField(
        default=1.1, null=False, blank=False)
    presionPrueba = models.FloatField(default=1.1, null=False, blank=False)
    perdidasPermisibles = models.FloatField(
        default=1.1, null=False, blank=False)
    capacidadManometros = models.FloatField(
        default=1.1, null=False, blank=False)
    capacidadBomba = models.FloatField(default=1.1, null=False, blank=False)
    fugaDetectadakm1 = models.FloatField(default=1.1, null=False, blank=False)
    fugaDetectadakm2 = models.FloatField(default=1.1, null=False, blank=False)
    fugaDetectadakm3 = models.FloatField(default=1.1, null=False, blank=False)
    fugaDetectadakm4 = models.FloatField(default=1.1, null=False, blank=False)
    presionesAlcanzadas = models.CharField(
        200, default="Indique presion", null=False, blank=False)
    fugarMayores = models.CharField(
        200, default="Indique fuga", null=False, blank=False)
    descripcionFuga = models.CharField(
        200, default="Descripcion fuga ", null=False, blank=False)
    accionesCorrectivas = models.CharField(
        200, default="Acción correctiva", null=False, blank=False)
    dictamen = models.CharField(
        200, default="Dictamen", null=False, blank=False)
    creado = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.nombreInspector} {self.apellidoInspector}"


class Proyecto(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(50)
    lugar = models.CharField(40)


def __str__(self):
    return f"{self.nombre}"


class Inspector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20, null=False, blank=True)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}  {self.telefono} {'|'} {self.telefono}2"


#