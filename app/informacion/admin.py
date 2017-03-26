from django.contrib import admin
# -*- coding: utf-8 -*-

from app.informacion.models import *

# Register your models here.

	
admin.site.register(fichas)
admin.site.register(estado_general)
admin.site.register(catalogo_enfermedades)
admin.site.register(codigo_expediente)
admin.site.register(Usuario)
admin.site.register(motivo_consulta)
admin.site.register(datos_generales)