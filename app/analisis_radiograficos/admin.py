from django.contrib import admin

# Register your models here.
from app.analisis_radiograficos.models import *


admin.site.register(aspectos_articulares)
admin.site.register(nance_general)
admin.site.register(nance_tablas)

admin.site.register(aspectos_mandibulares2)
admin.site.register(estadios_de_nolla)
admin.site.register(secuencia_y_cronologia)