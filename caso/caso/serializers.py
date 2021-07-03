from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cakehouse.models import Producto, Pago


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'id', 'nombre', 'descripcion', 'precio', 'stock', 'fecha']

class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pago
        fields = ['url', 'id', 'producto', 'nombre', 'segundo_n', 'apellido_p', 'apellido_m', 'direccion', 'casa_dpto', 'nro_casa', 'email', 'nro_telefono', 'pago']