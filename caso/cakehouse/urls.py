from django.urls import path

from . import views
app_name = 'cakehouse'
urlpatterns = [
    path('', views.index, name='index'),
    path('ver_productos', views.ver_productos, name='ver_productos'),
    path('pagar_productos', views.pagar_productos, name='pagar_productos'),
    path('guardar_pago', views.guardar_pago, name='guardar_pago'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('inicses', views.inicses, name='inicses'),
    path('logoutv', views.logoutv, name='logoutv'),
    path('indexadmin', views.indexadmin, name='indexadmin'),
]