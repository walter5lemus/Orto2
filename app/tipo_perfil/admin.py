from django.contrib import admin

from app.tipo_perfil.models import TipoPerfil, FacialFrontal, PerfilTotal   
from app.tipo_perfil.models import PTercioInferioir, Sonrisa, CompetenciaLabial

# Register your models here.
admin.site.register(TipoPerfil)
admin.site.register(FacialFrontal)
admin.site.register(PerfilTotal)
admin.site.register(PTercioInferioir)
admin.site.register(Sonrisa)
admin.site.register(CompetenciaLabial)

