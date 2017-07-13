from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect	
import json
from django.core import serializers
from app.citas.forms import *
from app.citas.models import *
from app.informacion.models import *
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

# Create your views here.
def citas_crear(request,codi,num):
	if fichas.objects.filter(cod_expediente=codi, numero=num).exists():
		user = request.user.id
		usuario = request.user.is_superuser
		usuario2=0
		if usuario:
			usuario2=1

		try:
			ids = fichas.objects.get(cod_expediente=codi,numero=num,completada=0)
			if ids:
				form = citasGeneralesForm(initial={'estudiante':request.user.username})
				form2 = citasForm(initial={})
				form3 = citasGeneralesForm2()
				form4 = citasForm2(initial={})
				return render(request, 'citas/citas_crear.html', {'form':form,'form2':form2,'form3':form3,'form4':form4,'usuario':usuario2,'codi':codi,'num':num})
		except Exception as e:
				return render(request, 'base/error_no_tiene_permiso_cerrada.html')
	else:
		return render(request, 'base/error_no_encontrado.html')

def citas_editar(request,codi,num):
	if fichas.objects.filter(cod_expediente=codi, numero=num).exists():
		user = request.user.id
		usuario = request.user.is_superuser
		usuario2=0
		if usuario:
			usuario2=1
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not datos_generales.objects.filter(cod_expediente=codi).exists():
					incompletos.append(0)
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-5)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-6)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-7)	
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-9)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
			form = citasGeneralesForm(initial={'estudiante':request.user.username})
			form2 = citasForm(initial={})
			form3 = citasGeneralesForm2()
			form4 = citasForm2(initial={})
			return render(request, 'citas/citas_editar.html', {'form':form,'form2':form2,'form3':form3,'form4':form4,'usuario':usuario2,'codi':codi,'num':num,'incompletos':incompletos})
	else:
		return render(request, 'base/error_no_encontrado.html')

def citas_editar2(request,codi,num,numeroCita):

	if request.user.is_superuser==1:
		if fichas.objects.filter(cod_expediente=codi, numero=num).exists():
			ids = fichas.objects.get(cod_expediente=codi,numero=num)
			if ids:
				datos_generale = datos_generales.objects.get(cod_expediente=codi)
				datosCitas = citas.objects.get(fichas_id=ids.id,num_cita=numeroCita)
				datosCitasGenerales = citas_general.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = citasGeneralesForm_editar(instance=datosCitasGenerales)
					form2 = citasForm(instance=datosCitas)
					return render(request, 'citas/citas_editar2.html', {'form':form,'form2':form2,'codi':codi,'num':num,'numeroCita':numeroCita,'nombre':datos_generale.nombre_completo})
				else:
					form = citasGeneralesForm(request.POST,instance=datosCitasGenerales)
					form2 = citasForm(request.POST,instance=datosCitas)
					if form.is_valid():
						form.save()
						form2.save()
					return redirect('/citas/editar/%s/%s/' %(codi,num))

		else:
			return render(request, 'base/error_no_encontrado.html')
	else:
		return render(request, 'base/error_no_hay_acceso.html')
def citas_consultar(request,codi,num):
	if fichas.objects.filter(cod_expediente=codi, numero=num).exists():
		user = request.user.id
		usuario = request.user.is_superuser
		usuario2=0
		if usuario:
			usuario2=1

		try:
			ids = fichas.objects.get(cod_expediente=codi,numero=num)
			if ids:
				incompletos =list()
				ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not datos_generales.objects.filter(cod_expediente=codi).exists():
					incompletos.append(0)
				if not motivo_consulta.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
				if not estado_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-2)
				if not TipoPerfil.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-3)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-4)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-5)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-6)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-7)	
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-9)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
				form = citasGeneralesForm(initial={'estudiante':request.user.username})
				form2 = citasForm(initial={})
				form3 = citasGeneralesForm2()
				form4 = citasForm2(initial={})
				return render(request, 'citas/citas_consultar.html', {'form':form,'form2':form2,'form3':form3,'form4':form4,'usuario':usuario2,'codi':codi,'num':num,'incompletos':incompletos})
		except Exception as e:
				return render(request, 'base/error_no_encontrado.html')
	else:
		return render(request, 'base/error_no_encontrado.html')	

def citas_crear2(request):
	
	user = request.user.id
	if request.method == 'POST':
		form2 = citasForm(request.POST,initial={})
		form = citasGeneralesForm(request.POST,initial={})
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return HttpResponseRedirect('/')
	else:

		form2 = citasForm(initial={})
		form = citasGeneralesForm(initial={'estudiante':request.user.username})
	return render(request, 'citas/citas_crear2.html', {'form':form,'form2':form2})

def post1(request):
	cod = request.POST['codigo']
	num = request.POST['numero']
	estudiante = request.POST['estudiante']
	aparato = request.POST['aparato']
	radioMx = request.POST['radio1']
	radioMd = request.POST['radio2']
	id_estudiante = Usuario.objects.get(username=estudiante)

	if request.method == 'POST':
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
			ids= fichas.objects.get(cod_expediente=cod,numero=num)
			citas_general.objects.create(aparato=aparato,fichas_id=ids.id,estudiante_id=id_estudiante.id,mx=radioMx,md=radioMd)
			return HttpResponse('<script>alert("cita creada con exito");</script>')
		else:
			return HttpResponse('No se encuentran fichas incompletas', status=401)

def eliminar_cita(request):
	cod = request.POST['codigo']
	num = request.POST['numero']
	numeroCita = request.POST['numeroCita']

	if request.method == 'POST':
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
			ids= fichas.objects.get(cod_expediente=cod,numero=num)
			if citas.objects.filter(fichas_id=ids.id,num_cita=numeroCita).exists():
				citas.objects.filter(fichas_id=ids.id,num_cita=numeroCita).delete()
				return HttpResponse('<script>alert("cita creada con exito");</script>')
			else:
				return HttpResponse('No se encuentran fichas incompletas', status=401)
		else:
			return HttpResponse('No se encuentran fichas incompletas', status=401)


def post2(request):
	cod = request.POST['codigo']
	num = request.POST['numero']
	resultados = request.POST['resultados']
	observaciones = request.POST['observaciones']
	fecha1 = request.POST['fecha1']
	fecha2 = request.POST['fecha2']

	num_cita=0
	if fichas.objects.filter(cod_expediente_id=cod,numero=num).exists():
		ids = fichas.objects.get(cod_expediente_id=cod,numero=num)
		try:
			numerocitas =  len(citas.objects.filter(fichas_id=ids.id))
			num_cita=numerocitas +1
		except Exception as e:
			raise e

		citas.objects.create(num_cita=num_cita,fecha_cita=fecha1,observaciones=observaciones,proxima_cita=fecha2,resultados=resultados,autorizacion=0,fichas_id=ids.id)


		return HttpResponse('<script>alert("cita creada con exito");</script>')
	else:
		return HttpResponse('No se encuentran fichas incompletas', status=401)


def autorizacion(request):
	cod = request.POST['codigo']
	num = request.POST['numero']

	print "entra"

	if request.method == 'POST':
		num_cita=1
		if fichas.objects.filter(cod_expediente_id=cod,numero=num).exists():
			ids = fichas.objects.get(cod_expediente_id=cod,numero=num)
			try:
				numerocitas =  len(citas.objects.filter(fichas_id=ids.id))
				num_cita=numerocitas
			except Exception as e:
				raise e
			citas.objects.filter(num_cita=numerocitas,fichas_id=ids.id).update(autorizacion=1,tutor=request.user.username)
			return HttpResponse('<script>alert("Se autorizo");</script>')
		else:
			return HttpResponse('Error', status=401)


class finalizar(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if request.method == 'GET':
				codigos = fichas.objects.filter(cod_expediente=cod,numero=num)
				for fi in codigos:
					if motivo_consulta.objects.filter(fichas_id=fi.id).exists():
						if estado_general.objects.filter(fichas_id=fi.id).exists():
							if TipoPerfil.objects.filter(fichas_id=fi.id).exists():
								if registro.objects.filter(fichas_id=fi.id).exists():
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
																			if imagenes_afmp.objects.filter(fichas_id=fi.id).exists():
																				fichas.objects.filter(id=fi.id).update(completada=1)
																				return HttpResponse('<script>alert("Se autorizo");</script>')
																			else:
																				return HttpResponse('Sin imagen AFMP', status=401)
																		else:
																			return HttpResponse('16', status=401)
																	else:
																		return HttpResponse('15', status=401)
																else:
																	return HttpResponse('14', status=401)
															else:
																return HttpResponse('13', status=401)
														else:
															return HttpResponse('12', status=401)
													else:
														return HttpResponse('11', status=401)
												else:
													return HttpResponse('10', status=401)
											else:
												return HttpResponse('9', status=401)
										else:
											return HttpResponse('8', status=401)
									else:
										return HttpResponse('7', status=401)	
								#else:
								#	return HttpResponse('4', status=401)
							else:
								return HttpResponse('3', status=401)
						else:
							return HttpResponse('2', status=401)
					else:
						return HttpResponse('1', status=401)


class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if request.method == 'POST':
			num_cita=0
			if fichas.objects.filter(cod_expediente_id=cod,numero=num).exists():
				ids = fichas.objects.get(cod_expediente_id=cod,numero=num)
				try:
					numerocitas =  len(citas.objects.filter(fichas_id=ids.id))
					num_cita=numerocitas
				except Exception as e:
					raise e
				citas.objects.filter(numero=numerocitas,fichas_id=ids.id).update(autorizacion=1)
				return HttpResponse('<script>alert("Se autorizo");</script>')
			else:
				return HttpResponse('No se encuentran fichas incompletas', status=401)



class BusquedaAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if datos_generales.objects.filter(cod_expediente=cod).exists():
			nombre = datos_generales.objects.filter(cod_expediente=cod)
			if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				if citas_general.objects.filter(fichas_id=ids.id).exists():
					citass = citas_general.objects.get(fichas_id=ids.id)
		else:
			nombre="fallo"
		data = serializers.serialize('json', nombre, fields=('nombre_completo'))
		return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				citass = citas_general.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', citass, fields=('aparato','md','mx'))
		return HttpResponse(data, content_type='application/json')


class BusquedaCitasListar(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
			ids= fichas.objects.get(cod_expediente=cod,numero=num)
			citas2 = citas.objects.filter(fichas_id=ids.id)
			data2 = serializers.serialize('json', citas2,fields=('codigo','num_cita','fecha_cita','observaciones','proxima_cita','resultados','autorizacion','tutor'))
		return HttpResponse(data2, content_type='application/json')



def registrocita(request,codi):
	user = request.user.id
	str(codi)
	entro = 0;
	
	num=0 
	queryset = citas_general.objects.filter(codigo_id=codi)
	if queryset:
		entro = 1
		num = len(queryset)
	#	return HttpResponseRedirect('/informacion/datos_generales/editar/%s/' %codi)
	
	if request.method == 'POST':
		if entro == 1:
			form2 = citasForm2(request.POST)
			if form2.is_valid():
				form2.save()
			return HttpResponseRedirect('/citas/cerrar/')
		else:
			
			form2 = citasForm2(request.POST)
			form = citasGeneralesForm2(request.POST)
			if form.is_valid() and form2.is_valid():
				form.save()
				form2.save()
			return HttpResponseRedirect('/citas/cerrar/')
	else:

		if entro ==	 1:
			form2 = citasForm2(initial={'codigo':codi,'num_cita':num+1})
			return render(request, 'citas/ventana2.html', {'form2':form2})	
		else:
			form = citasGeneralesForm2(initial={'codigo':codi,'estudiante':request.user.id})
			form2 = citasForm2(initial={'codigo':codi,'num_cita':num+1})
			
			return render(request, 'citas/ventana1.html', {'form':form,'form2':form2})
