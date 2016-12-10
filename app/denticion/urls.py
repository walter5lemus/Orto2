from django.conf.urls import url, include
from app.denticion.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
	url(r'^$', index, name= 'index'),
	url(r'^aspectos/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', denticion_view, name= 'denticion_crear'),
	url(r'^aspectos/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', denticion_editar, name= 'denticion_editar'),
	url(r'^aspectos/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', denticion_consultar, name= 'denticion_consultar'),

    url(r'^mordidas/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', mordidas_view, name= 'mordidas_crear'),
    url(r'^mordidas/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', mordidas_editar, name= 'mordidas_editar'),
    url(r'^mordidas/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', mordidas_consultar, name= 'mordidas_consultar'),
    
    url(r'^sagitales/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_crear), name='relacion_sagital_nuevo'),
	url(r'^listar$', login_required(relacionsagital_list), name='relacion_sagital_listar'),
	url(r'^sagitales/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_edit), name='relacion_sagital_editar'),
	url(r'^sagitales/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_consultar), name='relacion_sagital_consultar'),
]