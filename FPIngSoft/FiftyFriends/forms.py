from django.forms import ModelForm

from .models import administrador,platillo,c_tipo_platillo

class AdministradorForm(ModelForm):
    class Meta:
        model = administrador
        fields = ['id_administrador','nombre_usuario', 'contrasenia']

class PlatilloForm(ModelForm):
    class Meta:
        model = platillo
        fields = ['id_platillo','id_admin', 'id_tipo_platillo', 'descrpcion', 'precio', 'imagen']
