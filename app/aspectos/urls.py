from django.conf.urls import url, include
from app.aspectos.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index, name= 'index'),
	url(r'^denticion1/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion1_view), name= 'denticion1_crear'),
	url(r'^denticion1/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion1_editar), name= 'denticion1_editar'),
	url(r'^denticion1/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion1_consultar), name= 'denticion1_consultar'),
    url(r'^denticion1/eliminar/', login_required(EliminarAjaxView.as_view()), name='eliminar_registro'),
            
	url(r'^denticion2/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', denticion2_view, name= 'denticion2_crear'),
	url(r'^denticion2/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion2_editar), name= 'denticion2_editar'),
	url(r'^denticion2/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion2_consultar), name= 'denticion2_consultar'),
    url(r'^denticion2/eliminar/', login_required(Eliminar2AjaxView.as_view()), name='eliminar2_registro'),

	url(r'^denticion3/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion3_view), name= 'denticion3_crear'),
	url(r'^denticion3/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion3_editar), name= 'denticion3_editar'),    
	url(r'^denticion3/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(denticion3_consultar), name= 'denticion3_consultar'),
    url(r'^denticion3/eliminar/', login_required(EliminarAjaxView.as_view()), name='eliminar_registro3'),

	url(r'^mordidas/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(mordidas_view), name= 'mordidas_crear'),
	url(r'^mordidas/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(mordidas_editar), name= 'mordidas_editar'),
	url(r'^mordidas/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(mordidas_consultar), name= 'mordidas_consultar'),
    url(r'^mordidas/eliminar/', login_required(EliminarMordidasAjaxView.as_view()), name='eliminar_mordidas_registro'),


    url(r'^sagitales/nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_crear), name='relacion_sagital_nuevo'),
	url(r'^listar$', login_required(relacionsagital_list), name='relacion_sagital_listar'),
	url(r'^sagitales/editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_edit), name='relacion_sagital_editar'),
	url(r'^sagitales/consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(relacionsagital_consultar), name='relacion_sagital_consultar'),
 	url(r'^mostrar/$', login_required(MostrarImg.as_view())),
]
