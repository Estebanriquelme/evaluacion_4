from django.db import models
from django.db.models.base import Model
from django.utils.translation import ugettext as _

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=100, default='')
    precio = models.IntegerField(default=0)
    stock = models.BooleanField(default=False)
    fecha = models.DateField('fecha de creacion')

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('gerente', _('Gerente cakehouse')),
        )

class Pago(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, default='')
    segundo_n = models.CharField(max_length=70, default='')
    apellido_p = models.CharField(max_length=70, default='')
    apellido_m = models.CharField(max_length=70, default='')
    direccion = models.CharField(max_length=70, default='')
    casa_dpto = models.CharField(max_length=70, default='')
    nro_casa = models.CharField(max_length=70, default='')
    email = models.CharField(max_length=70, default='')
    nro_telefono = models.CharField(max_length=70, default='')
    pago = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('gerente', _('Gerente cakehouse')),
        )
