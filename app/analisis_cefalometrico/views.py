from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.http import HttpResponseRedirect	
from django.views.generic.base import RedirectView
from app.analisis_cefalometrico.forms import *
from app.analisis_cefalometrico.models import *
from app.informacion.models import *
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
codi="0000-00"

def cefalometrico_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			if analisis_cefalometrico.objects.filter(fichas_id=ids.id).exists():
				cefalometricoFormSet = modelformset_factory(analisis_cefalometrico, analisis_cefalometricoForm, extra=0)
				if ids:
					if request.method == 'GET':
						formset = cefalometricoFormSet(queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
					else:
						formset = cefalometricoFormSet(request.POST, request.FILES, queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
						if formset.is_valid():
							formset.save()
							fecha =timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/diag_cefalo/nuevo/%s/%s' % (codi, num))
					return render(request, 'analisis_cefalometrico/analisis_cefalometrico.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id})
			else:
				if ids:
					max_num=2
					cefalometricoFormSet = formset_factory(analisis_cefalometricoForm, extra=2, max_num=2)
					if request.method == 'POST':
						formset = cefalometricoFormSet(request.POST)
						if formset.is_valid():
							for form in formset:
								print form
								form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/diag_cefalo/nuevo/%s/%s' % (codi, num))
					else:
						formset = cefalometricoFormSet()
				return render(request, 'analisis_cefalometrico/analisis_cefalometrico.html', {'formset':formset, 'codi':codi, 'num':num,'ids':ids.id,'max':max_num})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	


def cefalometrico_editar(request, codi, num):
	str(codi)
	if request.user.is_superuser==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			cefalometricoFormSet = modelformset_factory(analisis_cefalometrico, analisis_cefalometricoForm, extra=0)
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
				if request.method == 'GET':
					formset = cefalometricoFormSet(queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
				else:
					formset = cefalometricoFormSet(request.POST, request.FILES, queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
					if formset.is_valid():
						formset.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/diag_cefalo/editar/%s/%s' % (codi, num))
					return render(request, 'analisis_cefalometrico/analisis_cefalometrico_editar.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id,'incompletos':incompletos})
				return render(request, 'analisis_cefalometrico/analisis_cefalometrico_editar.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id,'incompletos':incompletos})	
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
		except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
			else:
				return render(request, 'base/error_no_encontrado.html')	
	else:
		return render(request, 'base/error_no_hay_acceso.html')


def cefalometrico_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		cefalometricoFormSet = modelformset_factory(analisis_cefalometrico, analisis_cefalometricoForm_consultar, extra=0)
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
			if request.method == 'GET':
				formset = cefalometricoFormSet(queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
			else:
				formset = cefalometricoFormSet(request.POST, request.FILES, queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
				if formset.is_valid():
					formset.save()
				
				return redirect('/diag_cefalo/consultar/%s/%s' % (codi, num))			
			return render(request, 'analisis_cefalometrico/analisis_cefalometrico_consultar.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

		