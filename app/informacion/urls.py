from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.informacion.views import *

urlpatterns = [
	url(r'^inicio/nuevo/$', login_required(CodExpediente_crear), name='cod_expediente_crear'),

	url(r'^inicio/consultar/$', login_required(CodExpediente_consular), name='cod_expediente_consultar'),
	url(r'^inicio/editar/$', login_required(CodExpediente_editar), name='cod_expediente_editar'),

	url(r'^datos_generales/nuevo/$', login_required(DatosGeneral_crear), name='datos_generales_crear'),
	url(r'^datos_generales/nuevo2/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(DatosGeneral_crear2), name='datos_generales_crear2'),
	url(r'^datos_generales/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(DatosGenerales_consultar),name='datos_generales_consultar'),
	url(r'^datos_generales/consultar2/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(DatosGenerales_consultar2),name='datos_generales_consultar2'),
	url(r'^datos_generales/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(DatosGenerales_edit),name='datos_generales_editar'),


	url(r'^motivo_consultas/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(Motivo_Consulta_crear), name='motivo_consulta_crear'),
	url(r'^motivo_consultas/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(Motivo_Consulta_consultar),name='motivo_consulta_consultar'),
	url(r'^motivo_consultas/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(Motivo_Consulta_editar),name='motivo_consulta_editar'),

	url(r'^estado_general/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_crear), name='estado_general_crear'),
	url(r'^estado_general/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_edit),name='estado_general_editar'),
	url(r'^estado_general/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_consultar),name='estado_general_consultar'),
	url(r'^estado_general/editar2/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_edit2),name='estado_general_editar2'),

	url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
	url(r'^retiro/$', login_required(retiro_voluntario), name='retiro_voluntario'),
	url(r'^caducada/$', login_required(caducada), name='caducada'),


	url(r'^busqueda_ajax/$', login_required(BusquedaAjaxView.as_view())),
	url(r'^busqueda_ajax2/$', login_required(BusquedaAjaxView2.as_view())),
	url(r'^busqueda_ajax22/$', login_required(BusquedaAjaxView22.as_view())),
	url(r'^busqueda_ajax22_retiro/$', login_required(BusquedaAjaxView22_retiro.as_view())),
	url(r'^busqueda_ajax22_editar/$', login_required(BusquedaAjaxView22_editar.as_view())),
	url(r'^busqueda/$', login_required(busqueda), name='busquedaNombre'),
	url(r'^busqueda_admin/$', login_required(busqueda_admin), name='busquedaNombre'),
	url(r'^busqueda2/$', login_required(busqueda2), name='busquedaCodigo'),
	url(r'^busqueda2_admin/$', login_required(busqueda2_admin), name='busquedaCodigo'),	
	url(r'^codigo/$', login_required(busquedaCodigo.as_view()), name='busquedaCodigo'), 
	url(r'^eliminar_expediente/$', login_required(ajax_eliminar.as_view()), name="ajax_eliminar"),
	url(r'^eliminar_ficha/$', login_required(ajax_eliminar_ficha.as_view()), name="ajax_eliminar_ficha"),
	url(r'^retiro_voluntario/$', login_required(ajax_retiro_voluntario.as_view()), name="ajax_retiro_voluntario"),
	url(r'^caduca/$', login_required(ajax_caducada.as_view()), name="ajax_caducada"),




]