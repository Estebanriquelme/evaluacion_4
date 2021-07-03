from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Pago

# Create your views here.
def index(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos':listado_productos}
    return render(request,'cakehouse/index.html',carrito)

def ver_productos(request):
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    precio=request.POST['precio']
    return HttpResponse(nombre)