from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect	
from collections import OrderedDict
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

from app.analisis_cefalometrico.models import *
from app.analisis_radiograficos.models import *
from app.AnalisisDenticionMixta.models import *
from app.aspMandibular.models import *
from app.aspectos.models import *
from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.informacion.models import *
from app.tipo_perfil.models import *
from app.analisis_radiograficos.forms import *

codi=""

# Create your views here.

def AspectosArticulares_Crear(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
						incompletos.append(-2)
						incompletos.append(-3)
			if aspectos_articulares.objects.filter(fichas_id=ids.id).exists():
				estado = aspectos_articulares.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = AspectosArticularesForm(instance=estado)
				else:
					form = AspectosArticularesForm(request.POST, instance=estado)
					if form.is_valid():
						form.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return HttpResponseRedirect('/asp_mandibular1/nuevo/%s/%s/' %(codi,num))
				return render(request,'analisis_radiograficos/analisis_articulares.html',{'form':form,'codi': codi,'num':num,'incompletos':incompletos})
			else:
				if ids:
					if request.method == 'POST':
						form = AspectosArticularesForm(request.POST)
						if form.is_valid():
							form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
							return HttpResponseRedirect('/asp_mandibular1/nuevo/%s/%s/' %(codi,num))
						return render(request, 'analisis_radiograficos/analisis_articulares.html', {'form':form,'codi': codi,'num':num,'incompletos':incompletos})
					else:
						ids = fichas.objects.get(cod_expediente=codi, numero=num)
						form = AspectosArticularesForm(initial={'fichas':ids.id})
					return render(request, 'analisis_radiograficos/analisis_articulares.html', {'form':form,'codi': codi,'num':num,'incompletos':incompletos})
				return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	

def AspectosArticulares_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
			estado = aspectos_articulares.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = AspectosArticularesForm_consultar(instance=estado)
			else: 
				form = AspectosArticularesForm_consultar(request.POST, instance=estado)

				return HttpResponseRedirect('/asp_mandibular1/consultar/%s/%s/' %(codi,num))
			return render(request,'analisis_radiograficos/analisis_articulares_consultar.html', {'form':form,'codi': codi,'num':num,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')


def AspectosArticulares_edit(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-5)
						incompletos.append(-6)
						incompletos.append(-7)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-9)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-19)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-20)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-21)
			estado = aspectos_articulares.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = AspectosArticularesForm(instance=estado)
			else: 
				form = AspectosArticularesForm(request.POST, instance=estado)
				if form.is_valid():
					form.save()
					fecha=timezone.now()
					ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
					return HttpResponseRedirect('/asp_mandibular1/editar/%s/%s/' %(codi,num))
				return render(request,'analisis_radiograficos/analisis_articulares_editar.html',{'form':form,'codi': codi,'num':num,'incompletos':incompletos})
			return render(request,'analisis_radiograficos/analisis_articulares_editar.html',{'form':form,'codi': codi,'num':num,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	


# Otros Aspectos

def otrosAspectos_crear(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)
		incompletos =list()
		ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
		for fi in ficha:
			if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
					incompletos.append(-2)
					incompletos.append(-3)
		if aspectos_mandibulares2.objects.filter(fichas_id=ids.id).exists():
			estado = aspectos_mandibulares2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = aspectos_mandibulares2Form(instance=estado)
			else:
				form = aspectos_mandibulares2Form(request.POST, instance=estado)
				if form.is_valid():
					form.save()
					fecha=timezone.now()
					ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
					return redirect('/analisis_radiograficos/otrosHallazgos/nuevo/%s/%s/' % (codi, num))
			return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num,'incompletos':incompletos})

		else:
			if ids:
				if request.method == 'POST':
					form = aspectos_mandibulares2Form(request.POST, initial={'fichas': ids.id})
					if form.is_valid():
						form.save()
						fecha=timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return HttpResponseRedirect('/analisis_radiograficos/otrosHallazgos/nuevo/%s/%s/' % (codi, num))
					return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num,'incompletos':incompletos})
				else:
					form = aspectos_mandibulares2Form(initial={'fichas': ids.id})
			return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num,'incompletos':incompletos})
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	


def otrosAspectos_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
			datos = aspectos_mandibulares2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = aspectos_mandibulares2Form_consultar(instance=datos)
			else:
				form = aspectos_mandibulares2Form_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return redirect('/analisis_radiograficos/otrosHallazgos/consultar/%s/%s' % (codi, num))
		return render(request, 'analisis_radiograficos/otrosAspectosForm_consultar.html', {'form': form, 'codi': codi, 'num': num,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')


def otrosAspectos_editar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-5)
						incompletos.append(-6)
						incompletos.append(-7)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-9)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-19)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-20)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-21)
			estado = aspectos_mandibulares2.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = aspectos_mandibulares2Form(instance=estado)
			else:
				form = aspectos_mandibulares2Form(request.POST, instance=estado)
				if form.is_valid():
					form.save()
					fecha=timezone.now()
					ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
					return redirect('/analisis_radiograficos/otrosHallazgos/editar/%s/%s/' % (codi, num))
				return render(request, 'analisis_radiograficos/otrosAspectosForm_editar.html', {'form': form, 'codi': codi, 'num': num,'incompletos':incompletos})
			return render(request, 'analisis_radiograficos/otrosAspectosForm_editar.html', {'form': form, 'codi': codi, 'num': num,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	

# Otros Hallazgos

def otrosHallazgos_crear(request, codi, num):
	str(codi)
	try:
		incompletos =list()
		ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
		for fi in ficha:
			if not registro.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-1)
					incompletos.append(-2)
					incompletos.append(-3)		
		ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)
		if estadios_de_nolla.objects.filter(fichas_id=ids.id).exists():
			if secuencia_y_cronologia.objects.filter(fichas_id=ids.id).exists():
				estado1 = estadios_de_nolla.objects.get(fichas_id=ids.id)
				estado2 = secuencia_y_cronologia.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form1 = estadios_de_nollaForm(instance=estado1)
					form2 = secuencia_y_cronologiaForm(instance=estado2)
				else:
					form1 = estadios_de_nollaForm(request.POST, instance=estado1)
					form2 = secuencia_y_cronologiaForm(request.POST, instance=estado2)
					if (form1.is_valid() and form2.is_valid()):
						form1.save()
						form2.save()
						fecha=timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/analisis_cefalometrico/cefalometrico/nuevo/%s/%s' % (codi, num))
				return render(request, 'analisis_radiograficos/otrosHallazgosForm.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num,'incompletos':incompletos})            

		else:
			if ids:
				if request.method == 'POST':
					form1 = estadios_de_nollaForm(request.POST, initial={'fichas': ids.id})
					form2 = secuencia_y_cronologiaForm(request.POST, initial={'fichas': ids.id})
					if (form1.is_valid() and form2.is_valid() ):

						form1.save()
						form2.save()
						fecha=timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/analisis_cefalometrico/cefalometrico/nuevo/%s/%s' % (codi, num))
					return render(request, 'analisis_radiograficos/otrosHallazgosForm.html',{'form1': form1,'form2': form2, 'codi': codi, 'num': num,'incompletos':incompletos})
				else:
					form1 = estadios_de_nollaForm(initial={'fichas': ids.id})
					form2 = secuencia_y_cronologiaForm(initial={'fichas': ids.id})

			return render(request, 'analisis_radiograficos/otrosHallazgosForm.html',{'form1': form1,'form2': form2, 'codi': codi, 'num': num,'incompletos':incompletos})
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	


def otrosHallazgos_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
			datos1 = estadios_de_nolla.objects.get(fichas_id=ids.id)
			datos2 = secuencia_y_cronologia.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form1 = estadios_de_nollaConsultarForm(instance=datos1)
				form2 = secuencia_y_cronologiaConsultarForm(instance=datos2)
			else:
				form1 = estadios_de_nollaConsultarForm(request.POST, instance=datos1)
				form2 = secuencia_y_cronologiaConsultarForm(request.POST, instance=datos2)
				if (form1.is_valid() and form2.is_valid):
					form1.save()
					form2.save()
				return redirect('/analisis_cefalometrico/cefalometrico/consultar/%s/%s' % (codi, num))
		return render(request, 'analisis_radiograficos/otrosHallazgosForm_consultar.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')


def otrosHallazgos_editar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-5)
						incompletos.append(-6)
						incompletos.append(-7)
				if not diastemas_denticion.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-8)
				if not registro.objects.filter(fichas_id=fi.id).exists():
					if not registro.objects.filter(fichas_id=fi.id,problema_id=4).exists():
						incompletos.append(-9)
				if not sobremordidas.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-10)
				if not relaciones_sagitales.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-11)
				if not aspectos_articulares.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-12)
				if not aspectos_mandibulares1.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-13)
				if not aspectos_mandibulares2.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-14)
				if not estadios_de_nolla.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-15)
				if not analisis_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-16)
				if not diagnostico_cefalometrico.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-17)
				if not nance_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-18)
				if not moyers_inferior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-19)
				if not moyers_superior.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-20)
				if not diagnostico_general.objects.filter(fichas_id=fi.id).exists():
					incompletos.append(-21)
			estado1 = estadios_de_nolla.objects.get(fichas_id=ids.id)
			estado2 = secuencia_y_cronologia.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form1 = estadios_de_nollaForm(instance=estado1)
				form2 = secuencia_y_cronologiaForm(instance=estado2)
			else:
				form1 = estadios_de_nollaForm(request.POST, instance=estado1)
				form2 = secuencia_y_cronologiaForm(request.POST, instance=estado2)
				if (form1.is_valid() and form2.is_valid()):
					form1.save()
					form2.save()
					fecha=timezone.now()
					ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
					return redirect('/analisis_cefalometrico/cefalometrico/editar/%s/%s' % (codi, num))
				return render(request, 'analisis_radiograficos/otrosHallazgosForm_editar.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num,'incompletos':incompletos})
			return render(request, 'analisis_radiograficos/otrosHallazgosForm_editar.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	