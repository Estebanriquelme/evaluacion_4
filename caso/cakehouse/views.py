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
    listado = Producto.objects.filter(nombre__contains=nombre)
    carrito = {"listado" : listado}
    return render(request,'cakehouse/ver_productos.html',carrito)

def pagar_productos(request):
    nombre=request.POST['nombre']
    listado = Producto.objects.filter(nombre__contains=nombre)
    carrito = {"listado" : listado}
    return render(request,'cakehouse/pagar_productos.html',carrito)

def guardar_pago(request):
    nombre = request.POST['nombre']
    s_nombre = request.POST['s_nombre']
    apellido_p = request.POST['apellido_p']
    apellido_m = request.POST['apellido_m']
    direccion = request.POST['direccion']
    casadepto = request.POST['casadepto']
    numero_domi = request.POST['numero_domi']
    correo = request.POST['correo']
    numero_telefono = request.POST['numero_telefono']
    return HttpResponse(nombre+s_nombre+apellido_p+apellido_m)

def login(request):
    return render(request, 'cakehouse/login.html')
