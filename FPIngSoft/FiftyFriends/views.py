from django import forms
from django.db.models import QuerySet
from django.http import Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Count
from .models import administrador, c_ubicacion, orden, platillo, c_tipo_platillo, tableta,votacion
from .forms import AdministradorForm, PlatilloForm, NameForm

# ========== Login =========
def loggin_init(request):
    """
    Función que regresa la vista inicial
    para autenticarse como admin o ingresar
    los datos de la mesa y ubicación.
    """
    return render(request, 'EleUsuario.html', {})

def inicio(request):
    """
    Función utilitaria para redirigir a la vista de
    inicio.
    """
    return render(request, 'Inicio.html', {})

# ========== platillo CRUD=========3
def get_platillos() -> QuerySet:
    """
    Función utilitaria para recuperar todos los platillos
    de una orden dada.
    """
    orden_act = orden.objects.filter(id_orden=1)[0]
    return orden_act.id_platillos.all()

class Carrito(View):
    """
    Clase tipo vista para representar la
    lógica del carrito (orden).
    """
    def get(self, request, *args, **kwargs):
        """Método correspondiente a una request GET"""
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
        """Método correspondiente a una request POST"""
        form = NameForm(request.POST)

        cantidades = request.POST.getlist('cantidad[]')
        articulos =  request.POST.getlist('item[]')
        print(articulos)
        print(cantidades)

        total = 0.0
        for a,c in zip(articulos, cantidades):
            id_art = int(a)
            p = platillo.objects.filter(id_platillo=id_art).get()
            total += (float(p.precio) * float(c))

        print(total)
        ctxt = {
            'form': form,
            'total': total,
            'success': True
        }
        return render(request, 'carrito.html', ctxt)

    def agregar_platillo(request, cat, id_c, id_p):
        """Método utilitario para agregar un platillo al carrito."""
        carrito = orden.objects.filter(id_orden=1)[0]
        p = platillo.objects.filter(id_platillo=id_p).get()

        carrito.id_platillos.add(p)
        return redirect('carrito')

    def eliminar_platillo(request, id):
        """Método utilitario para eliminar un platillo al carrito."""
        carrito = orden.objects.filter(id_orden=1)[0]
        p = platillo.objects.filter(id_platillo=int(id))
        carrito.id_platillos.remove(p[0].id_platillo)

        return redirect('carrito')

class Menu(View):
    """
    Clase tipo vista para representar la
    lógica del menú.
    """
    def get(self, request, *args, **kwargs):
        """Método correspondiente a una request GET"""
        ctxt = {
            'platillos': platillo.objects.all()
        }
        return render(request, 'entradas-comensal.html', ctxt)

    def get_platillos_categoria(self, cat):
        """
        Método utilitario para devolver todos los platillos de una
        categoría dada.
        """
        id_cat = c_tipo_platillo.objects.filter(descripcion=cat).get()
        return platillo.objects.filter(id_tipo_platillo=id_cat.id_tipo_platillo)

    def categoria(request, cat):
        """
        Método utilitario para devolver la vista correspondiente en
        función del request.
        """
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
        """Método para regresar la vista individual de un platillo."""
        p = platillo.objects.filter(id_platillo=id_p).get()

        ctxt = {'platillo': p}
        return render(request, 'Platillos.html', ctxt)


class LogginRespTab(View):
    """
    Clase tipo vista para representar la
    lógica del menú.
    """
    def get(self, request):
        """Método correspondiente a una request GET"""
        return render(request, 'ModoResTableta.html')

    def post(self, request):
        """Método correspondiente a una request POST"""
        correo = request.POST['correoRes']
        psswrd = request.POST['contraseña']
        return redirect('ubicacion')

class Ubicacion(View):
    """
    Clase tipo vista para representar la
    lógica de las ubicaciones.
    """
    def get(self, request):
        """Método correspondiente a una request GET"""
        ubicaciones = c_ubicacion.objects.all()
        return render(request, 'UbicacionMesa.html', {'ubicaciones': ubicaciones})

    def post(self, request, *args, **kwargs):
        """Método correspondiente a una request POST"""
        form = NameForm(request.POST)
        print('POST request reached')
        mesas = request.POST.get('mesas')
        ubi =  request.POST.get('ubicacion') 
        
        if mesas.isdigit() and ubi != None:
            return redirect('inicio')
        return redirect('ubicacion')

class Votacion(View):
    """
    Clase tipo vista para representar la
    lógica de la votación de helado.
    """
    def get(self, request, *args, **kwargs):
        """Método correspondiente a una request GET"""
        votacion.objects.all().delete()
        sabores = platillo.objects.filter(id_tipo_platillo=4)
        ctxt = {
            'sabores': sabores,
        }

        return render(request, 'votacion.html',ctxt)
   
        
    def post(self, request, *args, **kwargs):
        """Método correspondiente a una request POST"""
        print('POST request reached')
        form = NameForm(request.POST)

        comensal = request.POST.getlist('nombreComensal')
        sabor =  request.POST.get('sabor') 
        if sabor != None:
            voto = votacion(nombre= comensal, helado = sabor)
            voto.save()

        
        sabores = platillo.objects.filter(id_tipo_platillo=4)
        ctxt = {
            'sabores': sabores,
            'form': form
        }

        return render(request, 'votacion.html',ctxt)

    def termina_voto(request):
        """Método para terminar la votación."""
        explicacion = votacion.objects.values('helado').order_by('helado').annotate(count=Count('helado')).order_by('-count')
        ganador = explicacion.first()
        ctxt = {
            'ganador': ganador,
            'explicacion': explicacion,
        }

        return render(request, 'resultados-votacion.html',ctxt)
