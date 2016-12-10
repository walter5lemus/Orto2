from django.conf.urls import url, include
from app.aspMandibular.views import asp_mandibular1, asp_mandibular1_view
from app.aspMandibular.views import asp_mandibular1_edit, asp_mandibular1_consultar
from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^$', asp_mandibular1, name='asp_mandibular1'),
   url(r'^nuevo/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(asp_mandibular1_view), name='asp_mandibular1_crear'),
   url(r'^edit/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(asp_mandibular1_edit), name='asp_mandibular1_edit'),
   url(r'^consultar/(?P<codi>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', login_required(asp_mandibular1_consultar), name='asp_mandibular1_consultar'),

]   