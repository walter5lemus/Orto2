from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.informacion.views import *

urlpatterns = [
	url(r'^inicio/nuevo/$', login_required(CodExpediente_crear), name='cod_expediente_crear'),
	url(r'^inicio/listar/', login_required(CodExpediente_List.as_view()),name='cod_expediente_listar'),

	url(r'^inicio/consultar/$', login_required(CodExpediente_consular), name='cod_expediente_consultar'),
	url(r'^inicio/editar/$', login_required(CodExpediente_editar), name='cod_expediente_editar'),

	url(r'^datos_generales/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(DatosGeneral_crear), name='datos_generales_crear'),
	url(r'^datos_generales/listar/', login_required(DatosGeneralesList.as_view()),name='datos_generales_listar'),
	url(r'^datos_generales/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(DatosGenerales_consultar),name='datos_generales_consultar'),
	url(r'^datos_generales/consultar2/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(DatosGenerales_consultar2),name='datos_generales_consultar2'),
	url(r'^datos_generales/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(DatosGenerales_edit),name='datos_generales_editar'),

	url(r'^fichas/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', login_required(Fichas_crear), name='fichas_crear'),
	url(r'^fichas/listar/', login_required(FichasList.as_view()),name='fichas_listar'),


	url(r'^estado_general/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_crear), name='estado_general_crear'),
	url(r'^estado_general/listar', login_required(EstadoGeneralList.as_view()),name='estado_general_listar'),
	url(r'^estado_general/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_edit),name='estado_general_editar'),
	url(r'^estado_general/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_consultar),name='estado_general_consultar'),
	url(r'^estado_general/editar2/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(EstadoGeneral_edit2),name='estado_general_editar2'),





]