from django.conf.urls import url, include
from app.diagCefalo.views import diag_cefalo, diag_cefalo_view 
from app.diagCefalo.views import diag_cefalo_edit, diag_cefalo_consultar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', diag_cefalo, name='diag_cefalo'),
    url(r'^nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(diag_cefalo_view), name='diag_cefalo_crear'),
    url(r'^editar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(diag_cefalo_edit), name='diag_cefalo_edit'),
    url(r'^consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(diag_cefalo_consultar), name='diag_cefalo_consultar'),

]