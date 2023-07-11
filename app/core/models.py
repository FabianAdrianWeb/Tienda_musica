from django.db import models
from django.contrib.auth.models import AbstractUser

# Definición del modelo Usuario que hereda de AbstractUser
class Usuario(AbstractUser):
    permisos = models.CharField(max_length=40, null=True, verbose_name="Permiso", default="1")  # Campo de tipo CharField para los permisos del usuario
    rut = models.CharField(max_length=40, null=True, verbose_name="Rut", default="")  # Campo de tipo CharField para el Rut del usuario

# Definición del modelo Producto
class Producto(models.Model):
    id = models.IntegerField(primary_key=True)  # Campo de tipo IntegerField como clave primaria para el Producto
    nomprod = models.CharField(max_length=100, null=False, blank=False)  # Campo de tipo CharField para el nombre del producto
    precio = models.IntegerField(null=False, blank=False)  # Campo de tipo IntegerField para el precio del producto
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    # Campo de tipo ImageField para la imagen del producto. Las imágenes se guardarán en la carpeta "images/" del servidor.
    # Si no se selecciona ninguna imagen, se establecerá una imagen predeterminada llamada "sinfoto.jpg".
    # No se permiten valores nulos ni en blanco.
    # El parámetro verbose_name se establece en "Imagen" para proporcionar una etiqueta legible para humanos al campo.
