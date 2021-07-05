from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Pago
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def index(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos':listado_productos}
    return render(request,'cakehouse/index.html',carrito)

def ver_productos(request):
    pk=request.POST['pk']
    listado = Producto.objects.filter(id=pk)
    carrito = {"listado" : listado}
    return render(request,'cakehouse/ver_productos.html',carrito)

def pagar_productos(request):
    pk=request.POST['pk']
    listado = Producto.objects.filter(id=pk)
    carrito = {"listado" : listado}
    return render(request,'cakehouse/pagar_productos.html',carrito)

def guardar_pago(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    s_nombre = request.POST['s_nombre']
    apellido_p = request.POST['apellido_p']
    apellido_m = request.POST['apellido_m']
    direccion = request.POST['direccion']
    casadepto = request.POST['casadepto']
    numero_domi = request.POST['numero_domi']
    correo = request.POST['correo']
    numero_telefono = request.POST['numero_telefono']
    precio = request.POST['precio']
    producto = Producto.objects.get(id=id)
    pago = Pago(nombre=nombre,segundo_n=s_nombre,apellido_p=apellido_p,apellido_m=apellido_m,direccion=direccion,
    casa_dpto=casadepto,email=correo,nro_casa=numero_domi,nro_telefono=numero_telefono,pago=precio)
    pago.producto=producto
    pago.save()
    return render(request,'cakehouse/index.html')

def iniciosesion(request):
    return render(request, 'cakehouse/iniciosesion.html')

def inicses(request):
    usuario = request.POST['usuario']
    clave = request.POST['clave']

    user = authenticate(request, username=usuario, password=clave)


    if user is not None:
        login(request, user)
        return render(request,'cakehouse/indexadmin.html')
    else:
        listado_productos = Producto.objects.all()
        carrito = {'listado_productos':listado_productos}
        messages.success(request,"usted no cuenta con una cuenta de administrador")
        return render(request,'cakehouse/index.html',carrito)

def logoutv(request):
    logout(request)
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos':listado_productos}
    return render(request,'cakehouse/index.html',carrito)

def indexadmin(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos':listado_productos}
    return render(request,'cakehouse/indexadmin.html',carrito)