from django.contrib import admin
from FiftyFriends.models import administrador, c_ubicacion, orden,platillo,c_tipo_platillo, tableta

admin.site.register(administrador)
admin.site.register(c_tipo_platillo)
admin.site.register(platillo)
admin.site.register(orden)
admin.site.register(tableta)
admin.site.register(c_ubicacion)
