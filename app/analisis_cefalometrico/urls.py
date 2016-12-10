from django.conf.urls import url, include
from app.analisis_cefalometrico.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^cefalometrico/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(cefalometrico_view), name= 'cefalometrico_crear'),
	url(r'^cefalometrico/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(cefalometrico_editar), name= 'cefalometrico_editar'),
	url(r'^cefalometrico/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(cefalometrico_consultar), name= 'cefalometrico_consultar'),
]