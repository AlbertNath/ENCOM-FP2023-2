from django.db import models
from typing import Dict

class administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_usuario
    
class c_tipo_platillo(models.Model):
    id_tipo_platillo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    def __str__(self):
        return self.descripcion

    
class c_ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    def __str__(self):
        return self.descripcion
    
class tableta(models.Model):
    from enum import Enum

    class UbicacionMesa(Enum):
        TERRAZA        = 1
        BALCON         = 2
        JARDIN         = 3
        COMEDORCENTRAL = 4

    id_tableta = models.AutoField(primary_key=True)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    numero_mesa = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=50)

    # def __init__(self, numero, ubicacion) -> None:
    #     self.numero = numero
    #     self.ubicacion = ubicacion

    @property
    def getNumero(self):
        return self.numero_mesa

    @property
    def setNumero(self, num: int):
        self.numero_mesa = num

    @property
    def getUbicacion(self):
        return self.ubicacion

    @property
    def setUbicacion(self, loc) -> None:
        self.ubicacion = loc

    def __str__(self):
        return self.id_tableta

class platillo(models.Model):
    id_platillo = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    descrpcion = models.CharField(max_length=300)
    precio = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    def __str__(self):
        return self.descrpcion
    
class orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_tableta = models.ForeignKey(tableta, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(platillo, on_delete=models.CASCADE)
    numero_mesa = models.IntegerField(default=0)

    # platillos
    _platillos: Dict[platillo, int] = {}
    _enviado: bool = False

    def agregarPlatillo(self, platillo, cantidad) -> None:
        # Esto parece tener sentido y ninguno a la vez :b
        # Debe ser muchos a muchos? En cuyo caso:
        # platillos_assoc = self.platillos.all().values('id_tipo_platillo')
        # categoria = []
        # for q in platilos_assoc:
        #   categoria.append(c_tipo_platillo.objects.filter(q['id_tipo_platillo']))
        #self.objects.filter(platillo.objects.filter(self.id_platillo))
        self._platillos.update({platillo: cantidad})


    def __str__(self):
        return self.id_orden
