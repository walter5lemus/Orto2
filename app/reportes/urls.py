from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.reportes.views import *

urlpatterns = [
	url(r'^reportes_diagnostico_general/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReportePersonasPDF.as_view()), name='generar_pdf'),
	url(r'^nuevo/$', login_required(reporte_crear), name='generar_pdf_nuevo'),
	url(r'^busqueda_ajax/$', login_required(BusquedaAjaxView.as_view())),
	url(r'^busqueda_ajax2/$', login_required(BusquedaAjaxView2.as_view())),
	url(r'^error/$', login_required(reporte_error), name='reporte_error'),

	url(r'^reporte_caducada/$', login_required(generar_pdf_Caducar), name='generar_pdf_caducada'),

	url(r'^reportes_imagenes/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes.as_view()), name='generar_pdf'),

	
]