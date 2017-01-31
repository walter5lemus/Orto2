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

from app.analisis_radiograficos.models import *
from app.analisis_radiograficos.forms import *

codi=""

# Create your views here.

def AspectosArticulares_Crear(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			if request.method == 'POST':
				form = AspectosArticularesForm(request.POST)
				if form.is_valid():
				 	form.save()

				return HttpResponseRedirect('/asp_mandibular1/nuevo/%s/%s/' %(codi,num))
				
			else:
				
				ids = fichas.objects.get(cod_expediente=codi, numero=num)
				form = AspectosArticularesForm(initial={'fichas':ids.id})
				
				return render(request, 'analisis_radiograficos/analisis_articulares.html', {'form':form,'codi': codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def AspectosArticulares_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = aspectos_articulares.objects.get(fichas_id=ids.id)
		 	if request.method == 'GET':
				form = AspectosArticularesForm_consultar(instance=estado)
			else: 
				form = AspectosArticularesForm_consultar(request.POST, instance=estado)

				return HttpResponseRedirect('/analisis_radiograficos/otrosAspectos/consultar/%s/%s/' %(codi,num))
			return render(request,'analisis_radiograficos/analisis_articulares.html', {'form':form,'codi': codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def AspectosArticulares_edit(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			estado = aspectos_articulares.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = AspectosArticularesForm(instance=estado)
			else: 
				form = AspectosArticularesForm(request.POST, instance=estado)
				if form.is_valid():
					form.save()
				return HttpResponseRedirect('/analisis_radiograficos/otrosAspectos/editar/%s/%s/' %(codi,num))
			return render(request,'analisis_radiograficos/analisis_articulares.html',{'form':form,'codi': codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

################################################################################################################


def nance_crear(request,codi,num):	
	str(codi)
	ids = fichas.objects.get(cod_expediente=codi, numero=num)


	max_numero=10
	nanceFormSet = formset_factory(nance_tabla, extra=max_numero, max_num=max_numero)
	nanceFormSet2 = formset_factory(nance_tabla, extra=max_numero, max_num=max_numero)

	if request.method == 'POST':

		form1 = nance_generalForm(request.POST,initial={'fichas':ids.id})
		formset = nanceFormSet(request.POST, request.FILES, prefix='1tablas')
		formset2 = nanceFormSet2(request.POST, request.FILES, prefix='2tablas')	
		if (form1.is_valid() and formset.is_valid() and formset2.is_valid() ):
		#if (formset.is_valid() ):
			form1.save()

			for form in formset:
				print form
				form.save()

			for form in formset2:
				print form
				form.save()	

		return redirect('/analisis_denticion_mixta/moyersinferior/nuevo/%s/%s/' %(codi,num))
	else:
			form1 = nance_generalForm(initial={'fichas':ids.id})
			formset = nanceFormSet(prefix='1tablas')
			formset2 = nanceFormSet2(prefix='2tablas')
	return render(request, 'analisis_radiograficos/analisis_nance.html', {'form1':form1, 'formset':formset, 'num':num,'formset2':formset2,'codi':codi,'ids':ids.id,'max':max_numero})		



def nance_consultar(request, codi, num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		nanceFormSet = modelformset_factory(nance_tablas, nance_tabla_consultar, extra=0)
		nanceFormSet2 = modelformset_factory(nance_tablas, nance_tabla_consultar, extra=0)
		max_numero=10
		if ids:
			nance_general1 = nance_general.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form1 = nance_generalForm_Consultar(instance=nance_general1)
				formset = nanceFormSet(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
				formset2 = nanceFormSet(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=2),prefix='2tablas')
			else:
				form1 = nance_generalForm_Consultar(request.POST, instance=nance_general1)
				formset = nanceFormSet(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
				formset2 = nanceFormSet2(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id, tabla=2),prefix='2tablas')

				return redirect('/analisis_denticion_mixta/moyersinferior/consultar/%s/%s/' %(codi,num))			
			return render(request, 'analisis_radiograficos/analisis_nance_consultar.html', {'form1':form1,'num':num,'formset':formset,'codi':codi,'formset2':formset2,'max':max_numero})	
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

def nance_editar(request, codi, num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	nanceFormSet = modelformset_factory(nance_tablas, nance_tabla, extra=0)
	nanceFormSet2 = modelformset_factory(nance_tablas, nance_tabla, extra=0)
	max_numero=10
	if ids:
		nance_general1 = nance_general.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form1 = nance_generalForm(instance=nance_general1)
			formset = nanceFormSet(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
			formset2 = nanceFormSet2(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=2),prefix='2tablas')
		else:
			form1 = nance_generalForm(request.POST, instance=nance_general1)
			formset = nanceFormSet(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
			formset2 = nanceFormSet2(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id, tabla=2),prefix='2tablas')

			#return redirect('/analisis_denticion_mixta/moyersinferior/editar/%s/%s/' %(codi,num))		
			return redirect('/')		
		return render(request, 'analisis_radiograficos/analisis_nance_editar.html', {'form1':form1,'formset':formset,'formset2':formset2,'codi':codi,'num':num,'max':max_numero})	
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
#	except Exception, e:
#		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

# Otros Aspectos

def otrosAspectos_crear(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
            if request.method == 'POST':
                form = aspectos_mandibulares2Form(request.POST, initial={'fichas': ids.id})
                if form.is_valid():
                    form.save()

                return HttpResponseRedirect('/analisis_radiograficos/otrosHallazgos/nuevo/%s/%s/' % (codi, num))
            else:
                form = aspectos_mandibulares2Form(initial={'fichas': ids.id})

        return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num})
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def otrosAspectos_consultar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
            datos = aspectos_mandibulares2.objects.get(fichas_id=ids.id)
            if request.method == 'GET':
                form = aspectos_mandibulares2Form_consultar(instance=datos)
            else:
                form = aspectos_mandibulares2Form_consultar(request.POST, instance=datos)
                if form.is_valid():
                    form.save()
                return redirect('/analisis_radiograficos/otrosHallazgos/consultar/%s/%s' % (codi, num))
        return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num})
        return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def otrosAspectos_editar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
            estado = aspectos_mandibulares2.objects.get(fichas_id=ids.id)
            if request.method == 'GET':
                form = aspectos_mandibulares2Form(instance=estado)
            else:
                form = aspectos_mandibulares2Form(request.POST, instance=estado)
                if form.is_valid():
                    form.save()
                return redirect('/analisis_radiograficos/otrosHallazgos/editar/%s/%s/' % (codi, num))
            return render(request, 'analisis_radiograficos/otrosAspectosForm.html', {'form': form, 'codi': codi, 'num': num})
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


# Otros Hallazgos

def otrosHallazgos_crear(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
            if request.method == 'POST':
                form1 = estadios_de_nollaForm(request.POST, initial={'fichas': ids.id})
                form2 = secuencia_y_cronologiaForm(request.POST, initial={'fichas': ids.id})
                if (form1.is_valid() and form2.is_valid() ):

                    form1.save()
                    form2.save()
                return redirect('/analisis_cefalometrico/cefalometrico/nuevo/%s/%s' % (codi, num))
            else:
                form1 = estadios_de_nollaForm(initial={'fichas': ids.id})
                form2 = secuencia_y_cronologiaForm(initial={'fichas': ids.id})

        return render(request, 'analisis_radiograficos/otrosHallazgosForm.html',{'form1': form1,'form2': form2, 'codi': codi, 'num': num})
    except Exception, e:
        return HttpResponse(e.__str__())


def otrosHallazgos_consultar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
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
        return render(request, 'analisis_radiograficos/otrosHallazgosForm.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num})
        return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def otrosHallazgos_editar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        if ids:
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
                return redirect('/analisis_cefalometrico/cefalometrico/editar/%s/%s' % (codi, num))
            return render(request, 'analisis_radiograficos/otrosHallazgosForm.html', {'form1': form1,'form2': form2, 'codi': codi, 'num': num})
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
    except Exception, e:
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
