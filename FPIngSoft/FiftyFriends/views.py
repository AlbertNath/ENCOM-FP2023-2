from django import forms
from django.http import Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import administrador, c_ubicacion, orden, platillo, c_tipo_platillo, tableta
from .forms import AdministradorForm, PlatilloForm, NameForm

# ========== Login =========

def getLoggin(request, *args, **kwargs):
    return render(request, 'login.html')

# Esto quizás debería ir por separado?
def iniciarSecion(request, nombre_usuario,contrasenia, template_name='books_pc_multi_view2/login.html'):
    admin = get_object_or_404(administrador, nombre_usuario = nombre_usuario ,contrasenia = contrasenia)
    ctx = {
        'admin': admin,
    }
    return render(request, template_name, ctx)

# ========== platillo CRUD=========3
def getPlatillos(self, request, *args, **kwargs):
    todos_los_platillos = platillo.objects.all()
    ctxt = {
        'platillos_totales': todos_los_platillos
    }
    return render(request, 'home.html', ctxt)

def verPlatillo(self, request, id_platillo, template_name='books_pc_multi_view2/platillo_view.html'):
    platillo = get_object_or_404(platillo, id_platillo=id_platillo)
    ctx = {
        'platillo': platillo
    }
    return render(request, template_name, ctx)

# Estaría mejor dejarlas fuera(?)
def getSeccion(request, c_tipo_platillo, template_name='books_pc_multi_view2/platillo_view.html'):
    id_tipo_platillo = get_object_or_404(platillo, c_tipo_platillo=c_tipo_platillo)
    platillos = get_object_or_404(platillo, id_tipo_platillo=id_tipo_platillo)
    ctx = {
        'platillos': platillos
    }
    return render(request, template_name, ctx)

def agregarPlatillo(request, template_name='books_pc_multi_view2/platillo_form.html'):
    form = PlatilloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('FiftyFriends:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def editarPlatillo(request, pk, template_name='books_pc_multi_view2/platillo_form.html'):
    platillo = get_object_or_404(platillo, id_platillo=id_platillo)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('FiftyFriends:home')
    ctx = {
        'form': form,
        'platillo': platillo,
    }
    return render(request, template_name, ctx)

def eliminarPlatillo(request, pk, template_name='books_pc_multi_view2platillo_form.html'):
    platillo = get_object_or_404(platillo, id_platillo=id_platillo)
    if request.method=='POST':
        platillo.delete()
        return redirect('FiftyFriends:home')
    ctx = {
        'object': book,
        'platillo': platillo,
    }
    return render(request, template_name, ctx)


class Carrito(View):
    def get(self, request, *args, **kwargs):
        orden_act = orden.objects.filter(id_orden=1)[0]

        platillos = orden_act.id_platillos.all()
        total = 0.0
        for i in platillos:
            total += float(i.precio)

        ctxt = {
            'platillos': platillos,
            'total': total,
        }

        return render(request, 'carrito.html', ctxt)

    def post(self, request, *args, **kwargs):
        print('POST request reached')
        form = NameForm(request.POST)

        cantidades = request.POST.getlist('cantidad[]')
        print(cantidades)

        ctxt = {
            'form': form,
            'success': True
        }
        return render(request, 'carrito.html', ctxt)

    def eliminar_platillo(request, id):
        carrito = orden.objects.filter(id_orden=1)[0]
        p = platillo.objects.filter(id_platillo=int(id))
        carrito.id_platillos.remove(p[0].id_platillo)

        return redirect('carrito')


def home(request):
    return render(request, 'Inicio.html', {})
