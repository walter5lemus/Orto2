from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.citas.views import *

urlpatterns = [
 url(r'^nuevo/', login_required(citas_crear), name= 'citasCrear'),


 url(r'^post1/', login_required(post1), name= 'post1'),
 

 url(r'^cerrar/', login_required(citas_crear2), name= 'citasCrear2'),
 url(r'^busqueda_ajax/$', login_required(BusquedaAjaxView.as_view())),
 url(r'^busqueda_ajax2/$', login_required(BusquedaAjaxView2.as_view())),
 url(r'^registro_cita/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$',login_required(registrocita)),
 url(r'^registro_listar_citas/$', login_required(BusquedaCitasListar.as_view())),
]