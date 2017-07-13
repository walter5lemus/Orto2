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
]