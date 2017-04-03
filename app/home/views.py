from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from collections import OrderedDict
from django.views.generic import TemplateView
from app.informacion.models import *
from app.informacion.forms import *
from django.core import serializers
from django.http import HttpResponse
import json
import time

from app.analisis_cefalometrico.models import *
from app.analisis_radiograficos.models import *
from app.AnalisisDenticionMixta.models import *
from app.aspMandibular.models import *
from app.aspectos.models import *
from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.informacion.models import *
from app.tipo_perfil.models import *

def index(request):
	user = request.user.id
	
	codigos = fichas.objects.filter(usuario_creador=user)
	for fi in codigos:
		if motivo_consulta.objects.filter(fichas_id=fi.id).exists():
			if estado_general.objects.filter(fichas_id=fi.id).exists():
				if TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					#if registro.objects.filter(fichas_id=fi.id).exists():
						#if registro_mordidas.objects.filter(fichas_id=fi.id).exists():
							#if relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					if aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
						if aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
							if aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
								if estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
									if analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
										if diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
											if nance_general.objects.filter(fichas_id=fi.id).exists():
												if moyers_inferior.objects.filter(fichas_id=fi.id).exists():
													if moyers_superior.objects.filter(fichas_id=fi.id).exists():
														if diagnostico_general.objects.filter(fichas_id=fi.id).exists():
															fichas.objects.filter(id=fi.id).update(completada=1)
	lista =list()
	numeros = list()
	ficha = fichas.objects.filter(usuario_creador=user, completada=0)
	for fi in ficha:
		lista.append(fi.numero)
		lista.append(fi.cod_expediente)
		
		numeros.append([fi.cod_expediente,fi.numero])
		if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
			lista.append(-1)
		if not estado_general.objects.filter(fichas_id=fi.id).exists():
			lista.append(-2)
		if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
			lista.append(-3)
		if not registro.objects.filter(fichas_id=fi.id).exists():
			lista.append(-4)
		if not registro_mordidas.objects.filter(fichas_id=fi.id).exists():
			lista.append(-5)
		if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
			lista.append(-6)
		if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
			lista.append(-7)
		if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
			lista.append(-8)
		if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
			lista.append(-9)
		if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
			lista.append(-10)
		if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
			lista.append(-11)
		if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
			lista.append(-12)
		if not nance_general.objects.filter(fichas_id=fi.id).exists():
			lista.append(-13)
		if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
			lista.append(-14)
		if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
			lista.append(-15)
		if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
			lista.append(-16)

	return render(request,'index.html',{'lista':lista,'ficha':ficha,'numeros':numeros})

	#return render(request,'index.html')

class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		user = request.user.id

		codigos = fichas.objects.filter(usuario_creador=user, completada=0)
		listaCod = list()

		for cod in codigos:
			print cod
			#listaCod.append(cod)
		data = serializers.serialize('json', datosGenerales, fields=('nombre_completo','fechaRegistro','fecha_hora_creacion','cod_expediente'))
		return HttpResponse(data, content_type='application/json')

