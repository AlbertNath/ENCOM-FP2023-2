from django.db import models

class administrador(models.Model):
    """Modelo para representar a un administrador."""
    id_administrador = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuario
    
class c_tipo_platillo(models.Model):
    """Modelo para representar a una categoría del menú."""
    id_tipo_platillo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.descripcion

    
class c_ubicacion(models.Model):
    """
    Modelo para representar una ubicación dentro del
    restaurante.
    """
    id_ubicacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.descripcion
    
class tableta(models.Model):
    """
    Modelo para representar una tableta del establecimiento.
    """
    id_tableta = models.AutoField(primary_key=True)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    numero_mesa = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_tableta)

class platillo(models.Model):
    """Modelo para representar un platillo del menú."""
    id_platillo = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    descrpcion = models.CharField(max_length=300)
    precio = models.CharField(max_length=50)
    imagen = models.TextField()

    def __str__(self):
        return self.descrpcion
    
class orden(models.Model):
    """Modelo para represenar una orden."""
    id_orden = models.AutoField(primary_key=True)
    id_tableta = models.ForeignKey(tableta, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(c_ubicacion, on_delete=models.CASCADE)
    id_tipo_platillo = models.ForeignKey(c_tipo_platillo, on_delete=models.CASCADE)
    id_admin = models.ForeignKey(administrador, on_delete=models.CASCADE)
    id_platillos = models.ManyToManyField(platillo)
    numero_mesa = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_orden)
        
class votacion(models.Model):
    """Modelo para representar la votación de helado."""
    nombre = models.TextField()
    helado = models.TextField()

    def __str__(self):
        return str(self.helado)
