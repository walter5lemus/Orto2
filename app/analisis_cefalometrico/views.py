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


codi="0000-00"

def cefalometrico_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)

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
				if request.method == 'GET':
					formset = cefalometricoFormSet(queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
				else:
					formset = cefalometricoFormSet(request.POST, request.FILES, queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
					if formset.is_valid():
						formset.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/diag_cefalo/edit/%s/%s' % (codi, num))
					return render(request, 'analisis_cefalometrico/analisis_cefalometrico.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id})
				return render(request, 'analisis_cefalometrico/analisis_cefalometrico.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id})	
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
		except Exception, e:
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	else:
		return render(request, 'base/error_no_hay_acceso.html')


def cefalometrico_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		cefalometricoFormSet = modelformset_factory(analisis_cefalometrico, analisis_cefalometricoForm_consultar, extra=0)
		if ids:
			if request.method == 'GET':
				formset = cefalometricoFormSet(queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
			else:
				formset = cefalometricoFormSet(request.POST, request.FILES, queryset=analisis_cefalometrico.objects.filter(fichas_id=ids.id))
				if formset.is_valid():
					formset.save()
				
				return redirect('/diag_cefalo/consultar/%s/%s' % (codi, num))			
			return render(request, 'analisis_cefalometrico/analisis_cefalometrico_consultar.html', {'formset':formset,'codi':codi,'num':num,'ids':ids.id,'completada':ids.completada})		
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')

		