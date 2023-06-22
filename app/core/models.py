from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    permisos = models.CharField(max_length=40,null=True, verbose_name="Permiso",default="1")
    rut = models.CharField(max_length=40,null=True, verbose_name="Rut",default="")

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nomprod = models.CharField(max_length=100, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
