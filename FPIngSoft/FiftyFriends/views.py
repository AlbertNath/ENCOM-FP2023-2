from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import administrador, c_ubicacion, orden, platillo, c_tipo_platillo, tableta
from .forms import AdministradorForm, PlatilloForm

# ========== Login =========
class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

# Esto quizás debería ir por separado?
def iniciarSecion(request, nombre_usuario,contrasenia, template_name='books_pc_multi_view2/login.html'):
    admin = get_object_or_404(administrador, nombre_usuario = nombre_usuario ,contrasenia = contrasenia)
    ctx = {
        'admin': admin,
    }
    return render(request, template_name, ctx)

# ========== platillo CRUD=========3
class Platillos(View):
    def get(self, request, *args, **kwargs):
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
        orden_act = orden.objects.filter(id_orden=0)

        id_platillos = orden_act.id_platillo.all()
        platillos_totales = []
        total = 0.0
        for i in id_platillos:
            p = platillo.objects.filter(id=i)
            platillos_totales.append(p)
            total += p.precio

        ctxt = {
            'platillos': platillos_totales
        }
        return render(request, 'carrito.html', ctxt)
