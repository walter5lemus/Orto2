from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from app.informacion.forms import *
from django.core import serializers
from django.http import HttpResponse

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
	#print user
	lista =list()
	numeros = list()
	ficha = fichas.objects.filter(usuario_creador=user)
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