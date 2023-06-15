"""
URL configuration for smartwelding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas de función
     1. Agregue una importación: desde las vistas de importación de my_app
     2. Agregue una URL a urlpatterns: ruta ('', vistas.inicio, nombre = 'inicio')
Vistas basadas en clases
     1. Agregue una importación: from other_app.views import Home
     2. Agrega una URL a urlpatterns: ruta('', Inicio.as_view(), nombre='inicio')
Incluir otra URLconf
     1. Importe la función include(): desde django.urls import include, ruta
     2. Agrega una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from smartwelding.views import miplantilla //asi tambien funciona
from .views import *
from . contacto import contacto, items
urlpatterns = [
    path("juntas/", include("juntas.urls")),
    path('admin/', admin.site.urls),
    path("plantilla/", view=miplantilla, ),
    path('contacto/', contacto, name='contacto'),
    path('items/', items, name='items'),
    path('Amateriales/', agregar_materiales_entregados, name='materiales_entregados')
]
