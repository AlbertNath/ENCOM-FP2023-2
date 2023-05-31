from django import forms
from django.db.models import QuerySet
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
def get_platillos() -> QuerySet:
    orden_act = orden.objects.filter(id_orden=1)[0]
    return orden_act.id_platillos.all()

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
        platillos = get_platillos()
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
        articulos =  request.POST.getlist('item[]')
        print(articulos)
        print(cantidades)

        ctxt = {
            'form': form,
            'total': 0,
            'success': True
        }
        return render(request, 'carrito.html', ctxt)

    def agregar_platillo(request, cat, id_c, id_p):
        carrito = orden.objects.filter(id_orden=1)[0]
        p = platillo.objects.filter(id_platillo=id_p).get()

        carrito.id_platillos.add(p)
        return redirect('carrito')

    def eliminar_platillo(request, id):
        carrito = orden.objects.filter(id_orden=1)[0]
        p = platillo.objects.filter(id_platillo=int(id))
        carrito.id_platillos.remove(p[0].id_platillo)

        return redirect('carrito')



class Menu(View):
    def get(self, request, *args, **kwargs):
        ctxt = {
            'platillos': platillo.objects.all()
        }
        return render(request, 'entradas-comensal.html', ctxt)

    def get_platillos_categoria(self, cat):
        id_cat = c_tipo_platillo.objects.filter(descripcion=cat).get()
        return platillo.objects.filter(id_tipo_platillo=id_cat.id_tipo_platillo)

def categoria(request, cat):
    m = Menu()
    match cat:
        case 'Entrada':
            platillos = m.get_platillos_categoria(cat)
            return render(request, 'entradas-comensal.html', {'platillos': platillos})
        case 'Principal':
            platillos = m.get_platillos_categoria(cat)
            return render(request, 'principales-comensal.html', {'platillos': platillos})
        case 'Bebida':
            platillos = m.get_platillos_categoria(cat)
            return render(request, 'bebidas-comensal.html', {'platillos': platillos})
        case 'Helado':
            platillos = m.get_platillos_categoria(cat)
            return render(request, 'helados-comensal.html', {'platillos': platillos})

    return redirect('..')

def get_platillo(request, cat, id_p, *args, **kwargs):
    p = platillo.objects.filter(id_platillo=id_p).get()

    ctxt = {'platillo': p}
    return render(request, 'Platillos.html', ctxt)

def inicio(request):
    return render(request, 'Inicio.html', {})
#Para probar y ver las vistas 
def modoAdmin(request) :
    return render(request, 'ModoAdmin.html', {})

def ubicacion(request) :
    return render(request, 'UbicacionMesa.html', {})

def EleUsuario(request) :
    return render(request, 'EleUsuario.html', {})

def ModoResTableta(request) :
    return render(request, 'ModoResTableta.html', {})

def platillos(request) :
    return render(request, 'Platillos.html', {})

def Modplatillos(request) :
    return render(request, 'ModPlatillos.html', {})

def Respuestas(request) :
    return render(request, 'Respuestas.html', {})

def entradasAdmin(request) :
    return render(request,'entradas-admin.html')
