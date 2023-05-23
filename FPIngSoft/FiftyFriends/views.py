from django.shortcuts import render, redirect, get_object_or_404
from .models import administrador,platillo,c_tipo_platillo
from .forms import AdministradorForm, PlatilloForm

# ========== Login =========

def iniciarSecion(request, nombre_usuario,contrasenia, template_name='books_pc_multi_view2/login.html'):
    admin = get_object_or_404(administrador, nombre_usuario = nombre_usuario ,contrasenia = contrasenia)
    ctx = {
        'admin': admin,
    }
    return render(request, template_name, ctx)

# ========== platillo CRUD=========3
def verPlatillo(request, id_platillo, template_name='books_pc_multi_view2/platillo_view.html'):
    platillo = get_object_or_404(platillo, id_platillo=id_platillo)
    ctx = {
        'platillo': platillo
    }
    return render(request, template_name, ctx)

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