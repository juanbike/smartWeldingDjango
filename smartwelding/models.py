from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
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
    especificacion =  models.CharField(max_length=30) 
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.especificacion}"
    
class Materiales(models.Model):
    tipo = models.CharField(max_length=40)
    shedule = models.CharField(max_length=4)
    tipoExtremo = models.CharField(max_length=15)
    tipoMaterial = models.CharField(max_length=30)     
    material = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo} {self.tipoMaterial}"
    
class Diametros(models.Model):
    nominal = models.CharField(max_length=4)
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
    tipoC = models.CharField(max_length=40)
    sheduleC = models.CharField(max_length=4)
    tipoExtremoC = models.CharField(max_length=15)
    tipoMaterialC = models.CharField(max_length=30)     
    materialC = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.tipoc} {self.tipoMaterialc}"

class MaterialesEntregados(models.Model):
    tipoE = models.CharField(max_length=40)
    sheduleE = models.CharField(max_length=4)
    tipoExtremoE = models.CharField(max_length=15)
    tipoMaterialE = models.CharField(max_length=30)     
    materialE = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.tipoE} {self.tipoMaterialE}"

class junta(models.Model):
   tipoJunta = models.CharField(max_length=20)
   linea = models.CharField(max_length=100)
   especificacion =  models.CharField(max_length=30)
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
    tramoKm = models.IntegerField()
    alKm = models.IntegerField()
    longitud = models.IntegerField()
    uniones = models.IntegerField()
    temperaturaAmbiente = models.FloatField()
    presionPrueba = models.FloatField()
    perdidasPermisibles = models.FloatField()
    capacidadManometros = models.FloatField()
    capacidadBomba = models.FloatField()
    fugaDetectadakm1 = models.FloatField()
    fugaDetectadakm2 = models.FloatField()
    fugaDetectadakm3 = models.FloatField()
    fugaDetectadakm4 = models.FloatField()
    presionesAlcanzadas = models.CharField(200)
    fugarMayores = models.CharField(200)
    descripcionFuga = models.CharField(200)
    accionesCorrectivas = models.CharField(200)
    dictamen = models.CharField(200)
    creado = models.DateTimeField(auto_now=True)

def __str__(self):
        return f"{self.nombreInspector} {self.apellidoInspector}"

