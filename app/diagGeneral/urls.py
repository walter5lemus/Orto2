from django.conf.urls import url, include
from app.diagGeneral.views import diag_general, diag_general_view
from app.diagGeneral.views import diag_general_edit, diag_general_consultar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', diag_general, name='diag_general'),
    url(r'^nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$',login_required(diag_general_view), name='diag_general_crear'),
    url(r'^edit/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(diag_general_edit), name='diag_general_edit'),
    url(r'^consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(diag_general_consultar), name='diag_general_consultar'),

]