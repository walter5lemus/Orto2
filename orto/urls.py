"""orto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app.home.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
# -*- coding: utf-8 -*-

urlpatterns = [
    #url(r"^$", direct_to_template, {"template": "index.html"}), 
    url(r'^$', RedirectView.as_view(url='/home/')),
	url(r'^home/', login_required(index),name='home'), 
    
    url(r'^admin/', admin.site.urls),
    url(r'^informacion/', include ('app.informacion.urls',namespace="informacion")),
    url(r'^tipo_perfil/', include ('app.tipo_perfil.urls',namespace="tipo_perfil")),
    url(r'^aspectos/', include ('app.aspectos.urls', namespace="aspectos")),
    url(r'^analisis_radiograficos/', include ('app.analisis_radiograficos.urls', namespace="analisis_radiograficos")),
    url(r'^accounts/login/',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',logout_then_login,name='logout'),
    url(r'^citas/', include ('app.citas.urls', namespace="citas")),
    url(r'^asp_mandibular1/', include ('app.aspMandibular.urls',namespace="asp_mandibular1")),
    url(r'^diag_cefalo/', include ('app.diagCefalo.urls',namespace="diag_cefalo")),
    url(r'^diag_general/', include ('app.diagGeneral.urls',namespace="diag_general")),
    url(r'^reportes/', include ('app.reportes.urls',namespace="reportes")),
    url(r'^analisis_cefalometrico/', include ('app.analisis_cefalometrico.urls', namespace="analisis_cefalometrico")),
    url(r'^analisis_denticion_mixta/', include ('app.AnalisisDenticionMixta.urls', namespace="analisis_denticion_mixta")),
    url(r'^gestor_img/', include ('app.gestorImg.urls', namespace="gestor_img")),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)