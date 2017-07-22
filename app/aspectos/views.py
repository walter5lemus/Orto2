from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from app.aspectos.forms import *
from app.aspectos.models import *
from django.core import serializers
from django.core.exceptions import ValidationError

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

def index(request):
	return render(request, 'aspectos/index.html')

def denticion1_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num, completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num, usuario_creador=request.user.id, completada=0):
			if ids:
				if tipo_denticion.objects.filter(fichas_id=ids.id).exists():
					max_num=5
					perdidaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
					anodonciaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
					mordidaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
					tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
					denticiones = denticion.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						perdida_formset = perdidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='1'), prefix='perdidas')
						anodoncia_formset = anodonciaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='2'), prefix='anodoncias')	
						mordida_formset = mordidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='3'), prefix='mordidas')
						form1 = tipo_denticionForm(instance=tipodenticion)
						form2 = denticionForm(instance=denticiones)
					else:
						perdida_formset = perdidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='perdidas',)		
						anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='anodoncias',)
						mordida_formset = mordidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='mordidas',)
						form1 = tipo_denticionForm(request.POST, instance=tipodenticion)
						form2 = denticionForm(request.POST, instance=denticiones)
						if (perdida_formset.is_valid() and anodoncia_formset.is_valid() and mordida_formset.is_valid() and form1.is_valid() and form2.is_valid()):
							form1.save()
							form2.save()

							for form in perdida_formset:
								form.save()
								
							for form in anodoncia_formset:
								form.save()				

							for form in mordida_formset:
								form.save()

						return redirect('/aspectos/denticion2/nuevo/%s/%s/' %(codi,num))
					return render(request, 'aspectos/dent1_form2.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'form2':form2, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
				else:
					max_num=5
					perdidaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
					anodonciaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
					mordidaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
					if request.method == 'POST':
						perdida_formset = perdidaFormSet(request.POST, request.FILES, prefix='perdidas')		
						anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, prefix='anodoncias')
						mordida_formset = mordidaFormSet(request.POST, request.FILES, prefix='mordidas')
						form1 = tipo_denticionForm(request.POST,initial={'fichas':ids.id})
						form2 = denticionForm(request.POST,initial={'fichas':ids.id})
						if (perdida_formset.is_valid() and anodoncia_formset.is_valid() and mordida_formset.is_valid() and form1.is_valid() and form2.is_valid()):
							form1.save()
							form2.save()
							for form in perdida_formset:
								form.save()

							for form in anodoncia_formset:
								form.save()

							for form in mordida_formset:
								form.save()					

						return redirect('/aspectos/denticion2/nuevo/%s/%s/' %(codi,num))
					else:
						perdida_formset = perdidaFormSet(prefix='perdidas')
						anodoncia_formset = anodonciaFormSet(prefix='anodoncias')
						mordida_formset = mordidaFormSet(prefix='mordidas')
						form1 = tipo_denticionForm(initial={'fichas':ids.id})
						form2 = denticionForm(initial={'fichas':ids.id})
						return render(request, 'aspectos/dent1_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'form2':form2, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')

def denticion1_editar(request,codi,num):
	str(codi)
	if request.user.is_superuser==1:
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
				max_num=5
				perdidaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
				anodonciaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
				mordidaFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
				tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
				denticiones = denticion.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					perdida_formset = perdidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='1'), prefix='perdidas')
					anodoncia_formset = anodonciaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='2'), prefix='anodoncias')	
					mordida_formset = mordidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='3'), prefix='mordidas')
					form1 = tipo_denticionForm(instance=tipodenticion)
					form2 = denticionForm(instance=denticiones)
				else:
					perdida_formset = perdidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='perdidas',)		
					anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='anodoncias',)
					mordida_formset = mordidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='mordidas',)
					form1 = tipo_denticionForm(request.POST, instance=tipodenticion)
					form2 = denticionForm(request.POST, instance=denticiones)
					if (perdida_formset.is_valid() and anodoncia_formset.is_valid() and mordida_formset.is_valid() and form1.is_valid() and form2.is_valid()):
						form1.save()
						form2.save()

						for form in perdida_formset:
							form.save()
							
						for form in anodoncia_formset:
							form.save()				

						for form in mordida_formset:
							form.save()

					return redirect('/aspectos/denticion2/editar/%s/%s/' %(codi,num))
				return render(request, 'aspectos/dent1_edit_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'form2':form2, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num,'incompletos':incompletos})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")		
		except Exception, e:
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	else:
		return render(request, 'base/error_no_hay_acceso.html')

class EliminarAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		ides = request.GET['ides']
		if registro.objects.filter(id=ides).exists():
			registro.objects.filter(id=ides).delete()

		return HttpResponse("Se elimino.")
		
def denticion1_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		perdidaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
		anodonciaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
		mordidaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
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
			tipo = tipo_denticion.objects.get(fichas_id=ids.id)
			denticiones = denticion.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				perdida_formset = perdidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='1'), prefix='perdidas')
				anodoncia_formset = anodonciaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='2'), prefix='anodoncias')
				mordida_formset = mordidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='3'), prefix='mordidas')
				form1 = tipo_denticionForm_consultar(instance=tipo)
				form2 = denticionForm(instance=denticiones)
			else:
				perdida_formset = perdidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='perdidas',)		
				anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='anodoncias',)
				mordida_formset = mordidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='mordidas',)
				form1 = denticionForm_consultar(request.POST, instance=tipo)
				form2 = denticionForm(request.POST, instance=denticiones)
			
				return redirect('/aspectos/denticion2/consultar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/dent1_cons_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'form2':form2, 'codi':codi,'num':num,'completada':ids.completada,'incompletos':incompletos})
		return render(request, 'base/error_no_encontrado.html')			
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

def denticion2_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num, completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num, usuario_creador=request.user.id, completada=0):
			if ids:
				if diastemas_denticion.objects.filter(fichas_id=ids.id).exists():
					max_num=5					
					diastemasFormSet = modelformset_factory(diastemas_denticion, diastemasForm, min_num=1, max_num=5, extra=0)
					tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						diastema_formset = diastemasFormSet(queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas')
						form1 = tipo_denticionForm2(instance=tipodenticion)
					else:
						diastema_formset = diastemasFormSet(request.POST, request.FILES, queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas',)		
						if (diastema_formset.is_valid()):
							for form in diastema_formset:
								form.save()

						return redirect('/aspectos/denticion3/nuevo/%s/%s/' %(codi,num))
					return render(request, 'aspectos/dent2_form2.html', {'diastema_formset':diastema_formset, 'form1':form1, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
				else:
					max_num=5					
					diastemasFormSet = formset_factory(diastemasForm, min_num=1, max_num=5, extra=0)
					tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
					if request.method == 'POST':					
						diastema_formset = diastemasFormSet(request.POST, request.FILES, prefix='diastemas')		
						if (diastema_formset.is_valid()):
							for form in diastema_formset:
								form.save()		

						return redirect('/aspectos/denticion3/nuevo/%s/%s/' %(codi,num))
					else:						
						diastema_formset = diastemasFormSet(prefix='diastemas')
						form1 = tipo_denticionForm2(instance=tipodenticion)
						return render(request, 'aspectos/dent2_form.html', {'diastema_formset':diastema_formset, 'form1':form1, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')

def denticion2_editar(request,codi,num):
	str(codi)
	if request.user.is_superuser==1:
		try:
			ids = fichas.objects.get(cod_expediente=codi, numero=num)
			if ids:
				max_num=5
				diastemasFormSet = modelformset_factory(diastemas_denticion, diastemasForm, min_num=1, max_num=5, extra=0)
				tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					diastema_formset = diastemasFormSet(queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas')
					form1 = tipo_denticionForm2(instance=tipodenticion)
				else:
					diastema_formset = diastemasFormSet(request.POST, request.FILES, queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas',)		
					if (diastema_formset.is_valid()):
						for form in diastema_formset:
							form.save()
						
					return redirect('/aspectos/denticion3/editar/%s/%s/' %(codi,num))
				return render(request, 'aspectos/dent2_edit_form.html', {'diastema_formset':diastema_formset, 'form1':form1, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")		
		except Exception, e:
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	else:
		return render(request, 'base/error_no_hay_acceso.html')

class Eliminar2AjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		ides = request.GET['ides']
		if diastemas_denticion.objects.filter(id=ides).exists():
			diastemas_denticion.objects.filter(id=ides).delete()

		return HttpResponse("Se elimino.")

def denticion2_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		diastemasFormSet = modelformset_factory(diastemas_denticion, diastemasForm_consultar, extra=0)
		if ids:
			tipo = tipo_denticion.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				diastema_formset = diastemasFormSet(queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas')
				form1 = tipo_denticionForm_consultar(instance=tipo)
			else:
				diastema_formset = diastemasFormSet(request.POST, request.FILES, queryset=diastemas_denticion.objects.filter(fichas_id=ids.id), prefix='diastemas',)		
				form1 = denticionForm_consultar(request.POST, instance=tipo)
			
				return redirect('/aspectos/denticion3/consultar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/dent2_cons_form.html', {'diastema_formset':diastema_formset, 'form1':form1, 'codi':codi,'num':num,'completada':ids.completada})
		return render(request, 'base/error_no_encontrado.html')			
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

def denticion3_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num, completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num, usuario_creador=request.user.id, completada=0):
			if ids:
				if registro.objects.filter(fichas_id=ids.id, problema='4').exists():
					max_num=5					
					numerariosFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
					tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						numerario_formset = numerariosFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='4'), prefix='numerarios')
						form1 = tipo_denticionForm2(instance=tipodenticion)
					else:
						numerario_formset = numerariosFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='numerarios',)		
						if (numerario_formset.is_valid()):
							for form in numerario_formset:
								form.save()

						return redirect('/aspectos/mordidas/nuevo/%s/%s/' %(codi,num))
					return render(request, 'aspectos/dent3_form2.html', {'numerario_formset':numerario_formset, 'form1':form1, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
				else:
					max_num=5					
					numerariosFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
					tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
					if request.method == 'POST':					
						numerario_formset = numerariosFormSet(request.POST, request.FILES, prefix='numerarios')		
						if (numerario_formset.is_valid()):
							for form in numerario_formset:
								form.save()		

						return redirect('/aspectos/mordidas/nuevo/%s/%s/' %(codi,num))
					else:						
						numerario_formset = numerariosFormSet(prefix='numerarios')
						form1 = tipo_denticionForm2(instance=tipodenticion)
						return render(request, 'aspectos/dent3_form.html', {'numerario_formset':numerario_formset, 'form1':form1, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')

def denticion3_editar(request,codi,num):
	str(codi)
	if request.user.is_superuser==1:
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
				max_num=5
				numerariosFormSet = modelformset_factory(registro, registroForm, min_num=1, max_num=5, extra=0)
				tipodenticion = tipo_denticion.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					numerario_formset = numerariosFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='4'), prefix='numerarios')
					form1 = tipo_denticionForm2(instance=tipodenticion)
				else:
					numerario_formset = numerariosFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='numerarios',)		
					if (numerario_formset.is_valid()):
						for form in numerario_formset:
							form.save()
						
					return redirect('/aspectos/mordidas/editar/%s/%s/' %(codi,num))
				return render(request, 'aspectos/dent3_edit_form.html', {'numerario_formset':numerario_formset, 'form1':form1, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num,'incompletos':incompletos})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")		
		except Exception, e:
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	else:
		return render(request, 'base/error_no_hay_acceso.html')

def denticion3_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		numerariosFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
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
			tipo = tipo_denticion.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				numerario_formset = numerariosFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='4'), prefix='numerarios')
				form1 = tipo_denticionForm_consultar(instance=tipo)
			else:
				numerario_formset = numerariosFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='numerarios',)		
				form1 = denticionForm_consultar(request.POST, instance=tipo)
			
				return redirect('/aspectos/mordidas/consultar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/dent3_cons_form.html', {'numerario_formset':numerario_formset, 'form1':form1, 'codi':codi,'num':num,'completada':ids.completada,'incompletos':incompletos})
		return render(request, 'base/error_no_encontrado.html')			
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

def mordidas_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num, completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num, usuario_creador=request.user.id, completada=0):
			if ids:
				if linea_media_facial.objects.filter(fichas_id=ids.id).exists():
					max_num=5
					mordidasFormSet = modelformset_factory(registro_mordidas, registro_mordidasForm, min_num=1, max_num=5, extra=0)
					lineamediafacial = linea_media_facial.objects.get(fichas_id=ids.id)
					sobremordida = sobremordidas.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						mordidas_formset = mordidasFormSet(queryset=registro_mordidas.objects.filter(fichas_id=ids.id), prefix='mordidas')
						form1 = linea_media_facialForm(instance=lineamediafacial)
						form2 = sobremordidasForm(instance=sobremordida)
					else:
						mordidas_formset = mordidasFormSet(request.POST, request.FILES, queryset=registro_mordidas.objects.filter(fichas_id=ids.id), prefix='mordidas',)		
						form1 = linea_media_facialForm(request.POST, instance=lineamediafacial)
						form2 = sobremordidasForm(request.POST, instance=sobremordida)
						if (mordidas_formset.is_valid() and form1.is_valid() and form2.is_valid()):
							form1.save()
							form2.save()

							for form in mordidas_formset:
								form.save()						

						return redirect('/aspectos/sagitales/nuevo/%s/%s/' %(codi,num))
					return render(request, 'aspectos/mordidas_form2.html', {'mordidas_formset':mordidas_formset, 'form1':form1, 'form2':form2, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
				else:
					max_num=5
					mordidasFormSet = formset_factory(registro_mordidasForm, min_num=1, max_num=5, extra=0)
					if request.method == 'POST':
						mordidas_formset = mordidasFormSet(request.POST, request.FILES, prefix='mordidas')		
						form1 = linea_media_facialForm(request.POST,initial={'fichas':ids.id})
						form2 = sobremordidasForm(request.POST,initial={'fichas':ids.id})
						if (mordidas_formset.is_valid() and form1.is_valid() and form2.is_valid()):
							form1.save()
							form2.save()
							for form in mordidas_formset:
								form.save()					

						return redirect('/aspectos/sagitales/nuevo/%s/%s/' %(codi,num))
					else:
						mordidas_formset = mordidasFormSet(prefix='mordidas')
						form1 = linea_media_facialForm(initial={'fichas':ids.id})
						form2 = sobremordidasForm(initial={'fichas':ids.id})
						return render(request, 'aspectos/mordidas_form.html', {'mordidas_formset':mordidas_formset, 'form1':form1, 'form2':form2, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')

class EliminarMordidasAjaxView(TemplateView):
	def get(self,request,*args,**kwargs):
		ides = request.GET['ides']
		if registro_mordidas.objects.filter(id=ides).exists():
			registro_mordidas.objects.filter(id=ides).delete()

		return HttpResponse("Se elimino.")

def mordidas_editar(request,codi,num):
	str(codi)
	ids = fichas.objects.get(cod_expediente=codi,numero=num)
	registro_mordidasFormSet = modelformset_factory(registro_mordidas, registro_mordidasForm, extra=1, max_num=5)
	if ids:
		max_num=5
		lineamediafacial = linea_media_facial.objects.get(fichas_id=ids.id)
		sobremordida = sobremordidas.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form1 = linea_media_facialForm(instance=lineamediafacial)
			form2 = sobremordidasForm(instance=sobremordida)
			formset = registro_mordidasFormSet(queryset=registro_mordidas.objects.filter(fichas_id=ids.id))
		else:
			form1 = linea_media_facialForm(request.POST, instance=lineamediafacial)
			form2 = sobremordidasForm(request.POST, instance=sobremordida)
			formset = registro_mordidasFormSet(request.POST, request.FILES, queryset=registro_mordidas.objects.filter(fichas_id=ids.id),)
			if form1.is_valid() and form2.is_valid() and formset.is_valid():
				form1.save()
				form2.save()
					
				for form in formset:
					form.save()
			return redirect('/aspectos/sagitales/editar/%s/%s/'%(codi,num))		
		return render(request, 'aspectos/denticion_edit_form.html', {'form1':form1,'form2':form2,'formset':formset, 'codi':codi,'num':num,'ids':ids.id,'max':max_num})	
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

def mordidas_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		registro_mordidasFormSet = modelformset_factory(registro_mordidas, registro_mordidasForm_consultar, extra=0)
		if ids:
			lineamediafacial = linea_media_facial.objects.get(fichas_id=ids.id)
			sobremordida = sobremordidas.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form1 = linea_media_facialForm_consultar(instance=lineamediafacial)
				form2 = sobremordidasForm_consultar(instance=sobremordida)
				formset = registro_mordidasFormSet(queryset=registro_mordidas.objects.filter(fichas_id=ids.id))
			else:
				form1 = linea_media_facialForm_consultar(request.POST, instance=lineamediafacial)
				form2 = sobremordidasForm_consultar(request.POST, instance=sobremordida)
				formset = registro_mordidasFormSet(request.POST, request.FILES, queryset=registro_mordidas.objects.filter(fichas_id=ids.id),)
				
				return redirect('/aspectos/sagitales/consultar/%s/%s/'%(codi,num))			
			return render(request, 'aspectos/denticion_cons_form.html', {'form1':form1,'form2':form2,'formset':formset, 'codi':codi,'num':num,'completada':ids.completada})	
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

def relacionsagital_crear(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			if ids:
				if relaciones_sagitales.objects.filter(fichas_id=ids.id).exists():
					relacionsagital = relaciones_sagitales.objects.get(fichas_id=ids.id)
					funcionmandibular = funcion_mandibular.objects.get(fichas_id=ids.id)
					imagenes = imagenes_afmp.objects.get(fichas_id=ids.id)
					if request.method == 'GET':
						form = RelacionSagitalForm(instance=relacionsagital)
						form2 = FuncionMandibularForm(instance=funcionmandibular)
						form3 = ImagenForm(instance=imagenes)
					else:
						form = RelacionSagitalForm(request.POST, instance=relacionsagital)
						form2 = FuncionMandibularForm(request.POST, instance=funcionmandibular)
						form3 = ImagenForm(request.POST, request.FILES, instance=imagenes)
						if form.is_valid() and form2.is_valid() and form3.is_valid():
							form.save()
							form2.save()
							form3.save()
						return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/nuevo/%s/%s/' %(codi,num))
					return render(request, 'aspectos/sagitales_form.html', {'form':form,'form2':form2,'form3':form3,'codi':codi,'num':num,})	
				else:
					if request.method == 'POST':
						form = RelacionSagitalForm(request.POST,initial={'fichas':ids.id})
						form2 = FuncionMandibularForm(request.POST,initial={'fichas':ids.id})
						form3 = ImagenForm(request.POST, request.FILES,initial={'fichas':ids.id})
						if form.is_valid() and form2.is_valid() and form3.is_valid():
							form.save()
							form2.save()
							form3.save()
						return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/nuevo/%s/%s/'%(codi,num))
					else:
						form = RelacionSagitalForm(initial={'fichas':ids.id})
						form2 = FuncionMandibularForm(initial={'fichas':ids.id})
						form3 = ImagenForm(initial={'fichas':ids.id})
				return render(request, 'aspectos/sagitales_form.html', {'form':form,'form2':form2,'form3':form3,'num':num,'codi':codi})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception as e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	

class MostrarImg(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		num = request.GET['numero']
		if fichas.objects.filter(cod_expediente=cod,numero=num).exists():
				ids= fichas.objects.get(cod_expediente=cod,numero=num)
				image = imagenes_afmp.objects.filter(fichas_id=ids.id)
				data = serializers.serialize('json', image, fields=('imagen'))
		return HttpResponse(data, content_type='application/json')

def relacionsagital_list(request):
	relacionsagital = relaciones_sagitales.objects.all().order_by('id')
	contexto = {'relaciones':relacionsagital}
	return render(request, 'aspectos/sagitales_list.html', contexto)

def relacionsagital_edit(request,codi,num):
	str(codi)
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
			relacionsagital = relaciones_sagitales.objects.get(fichas_id=ids.id)
			funcionmandibular = funcion_mandibular.objects.get(fichas_id=ids.id)
			imagenes = imagenes_afmp.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = RelacionSagitalForm(instance=relacionsagital)
				form2 = FuncionMandibularForm(instance=funcionmandibular)
				form3 = ImagenForm(instance=imagenes)
			else:
				form = RelacionSagitalForm(request.POST, instance=relacionsagital)
				form2 = FuncionMandibularForm(request.POST, instance=funcionmandibular)
				form3 = ImagenForm(request.POST, request.FILES, instance=imagenes)
				if form.is_valid() and form2.is_valid() and form3.is_valid():
					form.save()
					form2.save()
					form3.save()
				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/editar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/sagitales_editar_form.html', {'form':form,'form2':form2,'form3':form3,'codi':codi,'num':num,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')	

def relacionsagital_consultar(request,codi,num):
	str(codi)
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
			relacionsagital = relaciones_sagitales.objects.get(fichas_id=ids.id)
			funcionmandibular = funcion_mandibular.objects.get(fichas_id=ids.id)
			imagenes = imagenes_afmp.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = RelacionSagitalForm_consultar(instance=relacionsagital)
				form2 = FuncionMandibularForm_consultar(instance=funcionmandibular)
				form3 = ImagenForm_consultar(instance=imagenes)
			else: 
				form = RelacionSagitalForm_consultar(request.POST, instance=relacionsagital)
				form2 = FuncionMandibularForm_consultar(request.POST, instance=funcionmandibular)
				form3 = ImagenForm_consultar(request.POST, request.FILES, instance=imagenes)

				return HttpResponseRedirect('/analisis_radiograficos/aspectos_articulares/consultar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/sagitales_consultar_form.html', {'form':form,'form2':form2,'form3':form3,'codi':codi,'num':num,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

