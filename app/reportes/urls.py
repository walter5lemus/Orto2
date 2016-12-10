from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.reportes.views import *

urlpatterns = [
	url(r'^reportes/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReportePersonasPDF.as_view()), name='generar_pdf'),
	url(r'^nuevo/$', login_required(reporte_crear), name='generar_pdf_nuevo'),
	url(r'^nombre/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(BusquedaNombre.as_view()), name='busqueda_nombre'),
	url(r'^numero/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(BusquedaNumero.as_view()), name='busqueda_numero'),

]