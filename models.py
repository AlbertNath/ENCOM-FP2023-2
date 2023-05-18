from django.db import models

class administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_usuario
    
class c_tipo_platillo(models.Model):
    id_tipo_platillo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)

    
class c_ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    
class tableta(models.Model):
    id_tableta = models.AutoField(primary_key=True)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    numero_mesa = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

class platillo(models.Model):
    id_platillo = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    descrpcion = models.CharField(max_length=300)
    precio = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    
class orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_tableta = models.ForeignKey(tableta, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(platillo, on_delete=models.CASCADE)
    numero_mesa = models.CharField(max_length=50)
    