from django.conf.urls import url, include
from django.contrib import admin
from app.AnalisisDenticionMixta.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^moyerssuperior/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(moyerssup_view), name= 'moyerssuperior_crear'),
	url(r'^moyerssuperior/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(moyerssup_editar), name= 'oyerssuperior_editar'),
	url(r'^moyerssuperior/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(moyerssup_consultar), name= 'oyerssuperior_consultar'),
	url(r'^moyersinferior/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', moyersinf_view,name='moyerssuperior_crear'),
    url(r'^moyersinferior/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', moyersinf_editar,name='oyerssuperior_editar'),
    url(r'^moyersinferior/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', moyersinf_consultar,name='oyerssuperior_consultar'),
]