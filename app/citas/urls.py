from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.citas.views import *



urlpatterns = [
 url(r'^nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(citas_crear), name= 'citasCrear'),
 url(r'^editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(citas_editar), name= 'citaseditar'),

 url(r'^consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(citas_consultar), name= 'citasConsultar'),



 url(r'^post1/', login_required(post1), name= 'post1'),
 url(r'^post2/', login_required(post2), name= 'post2'),
 

 url(r'^autorizacion/', login_required(autorizacion), name= 'autorizacion'),
 url(r'^finalizar/', login_required(finalizar.as_view()), name= 'finalizar'),


 url(r'^cerrar/', login_required(citas_crear2), name= 'citasCrear2'),
 url(r'^busqueda_ajax/$', login_required(BusquedaAjaxView.as_view())),
 url(r'^busqueda_ajax2/$', login_required(BusquedaAjaxView2.as_view())),
 url(r'^registro_cita/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$',login_required(registrocita)),
 url(r'^registro_listar_citas/$', login_required(BusquedaCitasListar.as_view())),

]