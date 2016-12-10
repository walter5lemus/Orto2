from django.contrib import admin

from app.denticion.models import linea_media_facial
from app.denticion.models import sobremordidas
from app.denticion.models import registro_mordidas
from app.denticion.models import relaciones_sagitales
from app.denticion.models import funcion_mandibular

# Register your models here.

admin.site.register(linea_media_facial)
admin.site.register(sobremordidas)
admin.site.register(registro_mordidas)
admin.site.register(relaciones_sagitales)
admin.site.register(funcion_mandibular)