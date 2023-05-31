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
    path('admin/', admin.site.urls, name='admin'),
    path('inicio/', inicio, name='home'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/<str:cat>/', categoria, name='categoria'),
    path('menu/<int:id_p>/', get_platillo, name='verPlatillo'),
    path('menu/<int:id_c>/<int:id_p>/', Carrito.agregar_platillo, name='agregarPlatillo'),
    path('modoAdmin/', modoAdmin , name='Modo Admin'),
    path('ubicacion/', ubicacion, name='Ubicacion'),
    path('eleUsuario/', EleUsuario, name='EleccionUsuario'),
    path('modoResTableta/', ModoResTableta, name='ModoResTableta'),
    path('platillos/', platillos, name='Platillos'),
    path('Modplatillos/', Modplatillos, name='MoPlatillos'),
    path('respuestas/', Respuestas, name='Respuestas'),
    #path('tableta/', LoginTableta.as_view(), name='tableta'),
    #path('home/', Home.as_view(), name='home'),
    #path('home/<int:c_tipo_platillo>/', redir_seccion),
    #path('home/<int:platillo>/', vista_platillo),
    #path('votacion/', Votacion.as_view(), name='votacion'),
    #path('votacion/resultados', VotacionResult.as_view(), name='votacion'),
    #path('votacion/respuestas', VotacionResp.as_view(), name='votacion'),
    path('carrito/', Carrito.as_view(), name='carrito'),
    path('carrito/<int:id>/', Carrito.eliminar_platillo, name='eliminarPlatillo')
]
