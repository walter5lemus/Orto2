# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from app.gestorImg.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import url, include
from app.aspectos.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^paciente/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_paciente_crear), name='gestorImg_nuevo'),
    url(r'^paciente/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_paciente_editar), name='gestorImg_editar'),
    url(r'^paciente/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_paciente_consultar), name='gestorImg_consultar'),
	
	url(r'^paciente/mostrar/$', login_required(MostrarPaciente.as_view())),
	url(r'^paciente/mostrar2/$', login_required(MostrarPaciente2.as_view())),

	url(r'^radiograficas/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_radiograficas_crear), name='radiograficas_nuevo'),
    url(r'^radiograficas/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_radiograficas_editar), name='radiograficas_editar'),
    url(r'^radiograficas/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_radiograficas_consultar), name='radiograficas_consultar'),
	url(r'^radiograficas/mostrarr/$', login_required(MostrarRadiograficas.as_view())),

	url(r'^modelo/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_modelo_crear), name='modelo_nuevo'),
    url(r'^modelo/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_modelo_editar), name='modelo_editar'),
    url(r'^modelo/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_modelo_consultar), name='modelo_consultar'),
    url(r'^modelo/mostrarm/$', login_required(MostrarModelo.as_view())),

    url(r'^aparato/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_aparato_crear), name='aparato_nuevo'),
    url(r'^aparato/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_aparato_editar), name='aparato_editar'),
    url(r'^aparato/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(img_aparato_consultar), name='aparato_consultar'),
    url(r'^aparato/mostrara/$', login_required(MostrarAparato.as_view())),
]