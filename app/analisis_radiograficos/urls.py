from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.analisis_radiograficos.views import *

urlpatterns = [
    url(r'^aspectos_articulares/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(AspectosArticulares_Crear), name= 'aspectos_articulares_crear'),
    url(r'^aspectos_articulares/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(AspectosArticulares_consultar),name='aspectos_articulares_consultar'),
	url(r'^aspectos_articulares/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(AspectosArticulares_edit),name='aspectos_articulares_editar'),


	#OTROOS ASPECTOS

	url(r'^otrosAspectos/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',otrosAspectos_crear, name='otrosAspectos_crear'),
	url(r'^otrosAspectos/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',otrosAspectos_editar, name='otrosAspectos_editar'),
    url(r'^otrosAspectos/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', otrosAspectos_consultar, name='otrosAspectos_consultar'),

    #Otros Hallazgos

    url(r'^otrosHallazgos/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',otrosHallazgos_crear, name='otrosHallazgos_crear'),
    url(r'^otrosHallazgos/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',otrosHallazgos_consultar, name='otrosHallazgos_consultar'),
    url(r'^otrosHallazgos/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',otrosHallazgos_editar, name='otrosHallazgos_editar'),
]