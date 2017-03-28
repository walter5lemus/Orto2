from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from app.aspectos.forms import *
from app.aspectos.models import *

from app.informacion.models import *

codi="0000-00"

def index(request):
	return render(request, 'aspectos/index.html')

def denticion1_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			max_num=5
			perdidaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
			anodonciaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
			mordidaFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
			if request.method == 'POST':
				perdida_formset = perdidaFormSet(request.POST, request.FILES, prefix='perdidas')		
				anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, prefix='anodoncias')
				mordida_formset = mordidaFormSet(request.POST, request.FILES, prefix='mordidas')
				form1 = tipo_denticionForm(request.POST,initial={'fichas':ids.id})
				if (perdida_formset.is_valid() and anodoncia_formset.is_valid() and mordida_formset.is_valid() and form1.is_valid()):
					form1.save()
					for form in perdida_formset:
						print form
						form.save()

					for form in anodoncia_formset:
						print form
						form.save()

					for form in mordida_formset:
						print form
						form.save()					

				return redirect('/aspectos/mordidas/nuevo/%s/%s/' %(codi,num))
			else:
				perdida_formset = perdidaFormSet(prefix='perdidas')
				anodoncia_formset = anodonciaFormSet(prefix='anodoncias')
				mordida_formset = mordidaFormSet(prefix='mordidas')
				form1 = tipo_denticionForm(initial={'fichas':ids.id})
		return render(request, 'aspectos/dent1_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")		

def denticion1_editar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			max_num=5
			perdidaFormSet = modelformset_factory(registro, registroForm, extra=1, max_num=5)
			anodonciaFormSet = modelformset_factory(registro, registroForm, extra=1, max_num=5)
			mordidaFormSet = modelformset_factory(registro, registroForm, extra=1, max_num=5)
		
			denticion1 = denticion.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				perdida_formset = perdidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='1'), prefix='perdidas')
				anodoncia_formset = anodonciaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='2'), prefix='anodoncias')	
				mordida_formset = mordidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='3'), prefix='mordidas')
				form1 = denticionForm(instance=denticion1)
			else:
				perdida_formset = perdidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='perdidas',)		
				anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='anodoncias',)
				mordida_formset = mordidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='mordidas',)
				form1 = denticionForm(request.POST, instance=denticion1)
				if (perdida_formset.is_valid() and anodoncia_formset.is_valid() and mordida_formset.is_valid() and form1.is_valid()):
					for form in perdida_formset:
						print form
						form.save()				

					for form in anodoncia_formset:
						print form
						form.save()

					for form in mordida_formset:
						print form
						form.save()	

					form1.save()							
				return redirect('/denticion2/mordidas/editar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/dent1_edit_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1, 'codi':codi, 'num':num, 'ids':ids.id, 'max':max_num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")		
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
		
def denticion1_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		perdidaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
		anodonciaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
		mordidaFormSet = modelformset_factory(registro, registroForm_consultar, extra=0)
		if ids:
			denticion1 = denticion.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				perdida_formset = perdidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='1'), prefix='perdidas')
				anodoncia_formset = anodonciaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='2'), prefix='anodoncias')
				mordida_formset = mordidaFormSet(queryset=registro.objects.filter(fichas_id=ids.id, problema='3'), prefix='mordidas')
				form1 = denticionForm_consultar(instance=denticion1)
			else:
				perdida_formset = perdidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='perdidas',)		
				anodoncia_formset = anodonciaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='anodoncias',)
				mordida_formset = mordidaFormSet(request.POST, request.FILES, queryset=registro.objects.filter(fichas_id=ids.id), prefix='mordidas',)
				form1 = denticionForm_consultar(request.POST, instance=denticion1)
			
				return redirect('/denticion2/mordidas/consultar/%s/%s/' %(codi,num))
			return render(request, 'aspectos/dent1_cons_form.html', {'perdida_formset':perdida_formset, 'anodoncia_formset':anodoncia_formset, 'mordida_formset':mordida_formset, 'form1':form1,'codi':codi,'num':num})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")			
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
		
def denticion2_view(request,codi,num):
	str(codi)
	#try:
	ids = fichas.objects.get(cod_expediente=codi, numero=num)
	if ids:
		max_num=5
		diastemaFormSet = formset_factory(diastemasForm, min_num=1, max_num=5, extra=0)
		numerarioFormSet = formset_factory(registroForm, min_num=1, max_num=5, extra=0)
		if request.method == 'POST':
			diastema_formset = diastemaFormSet(request.POST, request.FILES, prefix='diatemas')		
			numerario_formset = numerarioFormSet(request.POST, request.FILES, prefix='numerarios')
			form1 = denticionForm(request.POST,initial={'fichas':ids.id})
			if (diastema_formset.is_valid() and numerario_formset.is_valid() and form1.is_valid()):
				form1.save()
				for form in diastema_formset:
					print form
					form.save()

				for form in numerario_formset:
					print form
					form.save()				

			return redirect('/aspectos/mordidas/nuevo/%s/%s/' %(codi,num))
		else:
			diastema_formset = diastemaFormSet(prefix='diastemas')
			numerario_formset = numerarioFormSet(prefix='numerarios')
			form1 = denticionForm(initial={'fichas':ids.id})
	return render(request, 'aspectos/dent2_form.html', {'diastema_formset':diastema_formset, 'numerario_formset':numerario_formset, 'form1':form1, 'codi':codi, "num":num, 'ids':ids.id, 'max':max_num})
	#except Exception, e:
		#return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")	

def mordidas_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			max_num=5
			registro_mordidasFormSet = formset_factory(registro_mordidasForm, extra=1, max_num=5)
			if request.method == 'POST':
				form1 = linea_media_facialForm(request.POST,initial={'fichas':ids.id})
				form2 = sobremordidasForm(request.POST,initial={'fichas':ids.id})
				formset = registro_mordidasFormSet(request.POST, request.FILES)		
				if (form1.is_valid() and form2.is_valid() and formset.is_valid()):
					form1.save()
					form2.save()
					
					for form in formset:
						print form
						form.save()

				return redirect('/aspectos/sagitales/nuevo/%s/%s/' %(codi,num))
			else:
				form1 = linea_media_facialForm(initial={'fichas':ids.id})
				form2 = sobremordidasForm(initial={'fichas':ids.id})
				formset = registro_mordidasFormSet()
		return render(request, 'aspectos/denticion_form.html', {'form1':form1, 'form2':form2, 'formset':formset, 'codi':codi,'num':num,'ids':ids.id,'max':max_num})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")	

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
					print form
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
			return render(request, 'aspectos/denticion_cons_form.html', {'form1':form1,'form2':form2,'formset':formset, 'codi':codi,'num':num,})	
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")

def relacionsagital_crear(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
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
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def relacionsagital_list(request):
	relacionsagital = relaciones_sagitales.objects.all().order_by('id')
	contexto = {'relaciones':relacionsagital}
	return render(request, 'aspectos/sagitales_list.html', contexto)

def relacionsagital_edit(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
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
			return render(request, 'aspectos/sagitales_editar_form.html', {'form':form,'form2':form2,'form3':form3,'codi':codi,'num':num,})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")


def relacionsagital_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi,numero=num)
		if ids:
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
			return render(request, 'aspectos/sagitales_consultar_form.html', {'form':form,'form2':form2,'form3':form3,'codi':codi,'num':num,})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

