from django.urls import path

from . import views
app_name = 'cakehouse'
urlpatterns = [
    path('', views.index, name='index'),
    path('ver_productos', views.ver_productos, name='ver_productos'),
]