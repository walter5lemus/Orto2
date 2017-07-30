from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from app.tipo_perfil.forms import Tipo_perfilForm,Tipo_perfilForm_consultar 
from app.analisis_cefalometrico.models import *
from app.analisis_radiograficos.models import *
from app.AnalisisDenticionMixta.models import *
from app.aspMandibular.models import *
from app.aspectos.models import *
from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.informacion.models import *
from app.tipo_perfil.models import *

def tipo_perfil(request):
	return render(request, 'tipo_perfil/tipo_perfil.html')



def tipo_perfil_view(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
		ultima = ultima_modificacion.objects.get(fichas_id=ids.id)
		if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
			incompletos =list()
			ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
			for fi in ficha:
				if not registro.objects.filter(fichas_id=fi.id).exists():
						incompletos.append(-1)
						incompletos.append(-2)
						incompletos.append(-3)
			if TipoPerfil.objects.filter(fichas_id=ids.id).exists():
				datos = TipoPerfil.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = Tipo_perfilForm(instance=datos)
				else: 
					form = Tipo_perfilForm(request.POST, instance=datos)
					if form.is_valid():
						form.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/aspectos/denticion1/nuevo/%s/%s' %(codi,num))
				return render(request, 'tipo_perfil/form_tipo_perfil.html',{'form':form,'num':num,'codi':codi,'fecha':ultima,'incompletos':incompletos}) 
			else:
				if ids:	
					if request.method == 'POST':
						form = Tipo_perfilForm(request.POST,initial={'fichas':ids.id})
						if form.is_valid():
							form.save()
							fecha =  timezone.now()
							ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
							return HttpResponseRedirect('/aspectos/denticion1/nuevo/%s/%s/' %(codi,num))
					else: 
						form = Tipo_perfilForm(initial={'fichas':ids.id})
						
				return render(request,'tipo_perfil/form_tipo_perfil.html', {'form':form,'codi':codi,'num':num,'fecha':ultima.fecha,'incompletos':incompletos})
		else:
			return render(request, 'base/error_no_tiene_permiso.html')
	except Exception, e:
		if int(num)>1:
			return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
		else:
			return render(request, 'base/error_no_encontrado.html')



def tipo_perfil_list(request):
	tipo_perfil = TipoPerfil.objects.all().order_by('fichas')
	contexto = {'tipo_perfiles': tipo_perfil}
	return render(request,'tipo_perfil/tipo_perfil_list.html', contexto)




def tipo_perfil_edit(request,codi,num):
	str(codi)
	if request.user.rol==1:
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
				datos = TipoPerfil.objects.get(fichas_id=ids.id)
				if request.method == 'GET':
					form = Tipo_perfilForm(instance=datos)
				else: 
					form = Tipo_perfilForm(request.POST, instance=datos)
					if form.is_valid():
						form.save()
						fecha =  timezone.now()
						ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
						return redirect('/aspectos/denticion1/editar/%s/%s' %(codi,num))
				return render(request, 'tipo_perfil/form_tipo_perfil_editar.html',{'form':form,'num':num,'codi':codi,'incompletos':incompletos})
			return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
		except Exception, e:
			if int(num)>1:
				return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
			else:
				return render(request, 'base/error_no_encontrado.html')	
	else:
		return render(request, 'base/error_no_hay_acceso.html')


def tipo_perfil_consultar(request,codi,num):
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
			datos = TipoPerfil.objects.get(fichas_id=ids.id)
			if request.method == 'GET':
				form = Tipo_perfilForm_consultar(instance=datos)
			else: 
				form = Tipo_perfilForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return HttpResponseRedirect('/aspectos/denticion1/consultar/%s/%s/' %(codi,num))
			return render(request, 'tipo_perfil/form_tipo_perfil_consultar.html',{'form':form,'num':num,'codi':codi,'completada':ids.completada,'incompletos':incompletos})
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return render(request, 'base/error_no_encontrado.html')


