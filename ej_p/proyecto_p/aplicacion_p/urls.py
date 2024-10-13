from django.contrib import admin
from django.urls import path
from .views import home, ficha_lista, servicio_lista

urlpatterns = [
    path('', home, name="home"),
    path('ficha_lista/', ficha_lista, name="ficha_lista"),
    path('servicio_lista/', servicio_lista,name="servicio_lista")
]
