"""FPIngSoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FiftyFriends.views import *

urlpatterns = [
    path('', loggin_init, name='loggin'),
    path('admin/', admin.site.urls, name='admin'),
    path('inicio/', inicio, name='inicio'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/<str:cat>/', Menu.categoria, name='categoria'),
    path('menu/<str:cat>/<int:id_p>/', Menu.get_platillo, name='verPlatillo'),
    path('menu/<str:cat>/<int:id_c>/<int:id_p>/', Carrito.agregar_platillo, name='agregarPlatillo'),
    path('ubicacion/', Ubicacion.as_view(), name='ubicacion'),
    path('modoResTableta/', LogginRespTab.as_view(), name='ModoResTableta'),
    path('votacion/', Votacion.as_view(), name='votacion'),
    path('carrito/', Carrito.as_view(), name='carrito'),
    path('carrito/<int:id>/', Carrito.eliminar_platillo, name='eliminarPlatillo'),
    path('cvotacion/', Votacion.termina_voto, name='terminaVoto')
]
