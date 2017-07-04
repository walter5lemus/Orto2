from django.conf.urls import url, include
from app.tipo_perfil.views import tipo_perfil, tipo_perfil_view, tipo_perfil_edit
from app.tipo_perfil.views import tipo_perfil_list,tipo_perfil_consultar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(tipo_perfil), name='tipo_perfil'),
    url(r'^nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(tipo_perfil_view), name='tipo_perfil_crear'),
    url(r'^editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(tipo_perfil_edit), name='tipo_perfil_edit'),
    url(r'^listar/$', login_required(tipo_perfil_list), name='tipo_perfil_listar'),
    url(r'^consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(tipo_perfil_consultar), name='tipo_perfil_consultar'),

]