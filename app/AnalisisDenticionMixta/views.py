from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.http import HttpResponseRedirect	
from django.views.generic.base import RedirectView
from app.AnalisisDenticionMixta.forms import *
from app.AnalisisDenticionMixta.models import *
from app.informacion.models import *
from django.forms import modelformset_factory

codi="0000-00"

def moyerssup_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			max_num=4
			moyerssupFormSet = formset_factory(moyersSupAncForm, extra=4, max_num=4)
			if request.method == 'POST':
				form1 = moyersSupForm(request.POST,initial={'fichas':ids.id})
				formset = moyerssupFormSet(request.POST)		
				if (form1.is_valid() and formset.is_valid()):
					form1.save()
					
					for form in formset:
						print form
						form.save()

				return redirect('/')
			else:
				form1 = moyersSupForm(initial={'fichas':ids.id})
				formset = moyerssupFormSet()
		return render(request, 'AnalisisDenticionMixta/moyerssuperior.html', {'form1':form1, 'formset':formset, 'num':num,'codi':codi,'ids':ids.id,'max':max_num})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	

def moyerssup_editar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		moyerssupFormSet = modelformset_factory(moyers_superior_ancho, moyersSupAncForm, extra=0)
			
		if ids:
			moysup = moyers_superior.objects.get(fichas_id=ids.id)
			if request.method == 'GET':				
				form1 = moyersSupForm(instance=moysup)
				formset = moyerssupFormSet(queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
			else:
				form1 = moyersSupForm(request.POST, instance=moysup)
				formset = moyerssupFormSet(request.POST, request.FILES, queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
				if form1.is_valid() and formset.is_valid():
					form1.save()
					formset.save()
				
				return redirect('/')			
			return render(request, 'AnalisisDenticionMixta/moyerssuperior.html', {'form1':form1,'formset':formset,'num':num,'codi':codi,'ids':ids.id})	
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

def moyerssup_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		moyerssupFormSet = modelformset_factory(moyers_superior_ancho, moyersSupAncForm_consultar, extra=0)
		if ids:
			moysup = moyers_superior.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form1 = moyersSupForm_consultar(instance=moysup)
				formset = moyerssupFormSet(queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
			else:
				form1 = moyersSupForm(request.POST, instance=moysup)
				formset = moyerssupFormSet(request.POST, request.FILES, queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
					
				return redirect('/')			
			return render(request, 'AnalisisDenticionMixta/moyerssuperior_consultar.html', {'form1':form1,'formset':formset,'num':num,'codi':codi,'ids':ids.id})	
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

def moyersinf_view(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
            max_num = 4
            moyersinfFormSet = formset_factory(moyersInfAncForm, extra=4, max_num=4)
            if request.method == 'POST':
                form1 = moyersInfForm(request.POST, initial={'fichas': ids.id})
                formset = moyersinfFormSet(request.POST)
                if (form1.is_valid() and formset.is_valid()):
                    form1.save()

                    for form in formset:
                        print form
                        form.save()

                return redirect('/analisis_denticion_mixta/moyerssuperior/nuevo/%s/%s/' %(codi,num))
            else:
                form1 = moyersInfForm(initial={'fichas': ids.id})
                formset = moyersinfFormSet()
        return render(request, 'AnalisisDenticionMixta/moyersinferior.html',{'form1': form1, 'formset': formset, 'codi': codi, 'ids': ids.id, 'num':num,'max': max_num})
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def moyersinf_editar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        moyersinfFormSet = modelformset_factory(moyers_inferior_ancho, moyersInfAncForm, extra=0)

        if ids:
            moyinf = moyers_inferior.objects.get(fichas_id=ids.id)
            if request.method == 'GET':
                form1 = moyersInfForm(instance=moyinf)
                formset = moyersinfFormSet(queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
            else:
                form1 = moyersInfForm(request.POST, instance=moyinf)
                formset = moyersinfFormSet(request.POST, request.FILES,
                                           queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
                if form1.is_valid() and formset.is_valid():
                    form1.save()
                    formset.save()

                return redirect('/analisis_denticion_mixta/moyerssuperior/editar/%s/%s/' %(codi,num))
            return render(request, 'AnalisisDenticionMixta/moyersinferior.html',
                          {'form1': form1, 'formset': formset, 'codi': codi,'num':num, 'ids': ids.id})
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")


def moyersinf_consultar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        moyersinfFormSet = modelformset_factory(moyers_inferior_ancho, moyersInfAncForm_consultar, extra=0)
        if ids:
            moyinf = moyers_inferior.objects.get(fichas_id=ids.id)
            if request.method == 'GET':
                form1 = moyersInfForm_consultar(instance=moyinf)
                formset = moyersinfFormSet(queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
            else:
                form1 = moyersInfForm(request.POST, instance=moyinf)
                formset = moyersinfFormSet(request.POST, request.FILES,
                                           queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
                if form1.is_valid() and formset.is_valid():
                    form1.save()
                    formset.save()
                return redirect('/analisis_denticion_mixta/moyerssuperior/consultar/%s/%s/' %(codi,num))
            return render(request, 'AnalisisDenticionMixta/moyersinferior_consultar.html',
                          {'form1': form1, 'formset': formset, 'codi': codi,'num':num, 'ids': ids.id})
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
