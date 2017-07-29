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
	url(r'^error_imagenes/$', login_required(reporte_error_imagenes), name='reporte_error_imagenes'),
	url(r'^error_no_encontrado/$', login_required(reporte_error_no_existe), name='reporte_error_no_existe'),

	url(r'^reporte_caducada/$', login_required(generar_pdf_Caducar), name='generar_pdf_caducada'),

	url(r'^reportes_imagenes/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes.as_view()), name='generar_pdf_imagenes'),
	url(r'^reportes_imagenes2/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes2.as_view()), name='generar_pdf_imagenes2'),
	url(r'^reportes_imagenes_modelo/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Modelo.as_view()), name='reportes_imagenes_modelo'),
	url(r'^reportes_imagenes_radiograficas_panoramica_inicial/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_panoramica_inicial.as_view()), name='ReporteImagenes_Radiograficas_panoramica_inicial'),
	url(r'^reportes_imagenes_radiograficas_panoramica_trazados/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_panoramica_trazados.as_view()), name='ReporteImagenes_Radiograficas_panoramica_trazados'),
	url(r'^reportes_imagenes_radiograficas_panoramica_seguimiento/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_panoramica_seguimiento.as_view()), name='ReporteImagenes_Radiograficas_panoramica_seguimiento'),


	url(r'^reportes_imagenes_radiograficas_cefalometrica_inicial/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_cefalometrica_inicial.as_view()), name='ReporteImagenes_Radiograficas_cefalometrica_inicial'),
	url(r'^reportes_imagenes_radiograficas_cefalometrica_trazados/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_cefalometrica_trazados.as_view()), name='ReporteImagenes_Radiograficas_cefalometrica_trazados'),
	url(r'^reportes_imagenes_radiograficas_cefalometrica_seguimiento/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(ReporteImagenes_Radiograficas_cefalometrica_seguimiento.as_view()), name='ReporteImagenes_Radiograficas_cefalometrica_seguimiento'),

	
]