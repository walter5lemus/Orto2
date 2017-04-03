from django.conf.urls import url, include
from app.aspMandibular.views import asp_mandibular1, asp_mandibular1_view
from app.aspMandibular.views import asp_mandibular1_edit, asp_mandibular1_consultar
from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^$', login_required(index), name='home1'),
]   