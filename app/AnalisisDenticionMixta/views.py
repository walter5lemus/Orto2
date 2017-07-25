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

################################################################################################################

def nance_crear(request,codi,num):  
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num,completada=0)
        max_numero=10
        incompletos =list()
        ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
        for fi in ficha:
            if not registro.objects.filter(fichas_id=fi.id).exists():
                    incompletos.append(-1)
                    incompletos.append(-2)
                    incompletos.append(-3)        
        if fichas.objects.filter(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0):
            if nance_tablas.objects.filter(fichas_id=ids.id).exists():
                if nance_tablas.objects.filter(fichas_id=ids.id).exists():
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
                            formset2 = nanceFormSet2(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=2),prefix='2tablas')

                            if (form1.is_valid() and formset.is_valid() and formset2.is_valid()):
                                form1.save()
                                
                                for form in formset:
                                    
                                    form.save()
                                for form in formset2:
                                       form.save()
                                fecha =  timezone.now()
                                ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                                return redirect('/analisis_denticion_mixta/moyersinferior/nuevo/%s/%s/' %(codi,num)) 
                            else:
                                
                                return render(request, 'AnalisisDenticionMixta/analisis_nance_editar.html', {'form1':form1,'formset':formset,'formset2':formset2,'codi':codi,'num':num,'max':max_numero,'ids':ids.id,'incompletos':incompletos})   
                        return render(request, 'AnalisisDenticionMixta/analisis_nance2.html', {'form1':form1,'formset':formset,'formset2':formset2,'codi':codi,'num':num,'max':max_numero,'ids':ids.id,'incompletos':incompletos})   
                    return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
            else:
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
                            form.save()

                        for form in formset2:
                            form.save()
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                    else:
                        messages.error(request, "Error")
                        return render(request, 'AnalisisDenticionMixta/analisis_nance_error.html', {'form':form_class()})

                    return redirect('/analisis_denticion_mixta/moyersinferior/nuevo/%s/%s/' %(codi,num))
                else:
                        form1 = nance_generalForm(initial={'fichas':ids.id})
                        formset = nanceFormSet(prefix='1tablas')
                        formset2 = nanceFormSet2(prefix='2tablas')
                return render(request, 'AnalisisDenticionMixta/analisis_nance.html', {'form1':form1, 'formset':formset, 'num':num,'formset2':formset2,'codi':codi,'ids':ids.id,'max':max_numero,'incompletos':incompletos})       
        else:
            return render(request, 'base/error_no_tiene_permiso.html')
    except Exception, e:
        if int(num)>1:
            return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
        else:
            return render(request, 'base/error_no_encontrado.html') 


def nance_consultar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        nanceFormSet = modelformset_factory(nance_tablas, nance_tabla_consultar, extra=0)
        nanceFormSet2 = modelformset_factory(nance_tablas, nance_tabla_consultar, extra=0)
        max_numero=10
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
            return render(request, 'AnalisisDenticionMixta/analisis_nance_consultar.html', {'form1':form1,'num':num,'formset':formset,'codi':codi,'formset2':formset2,'max':max_numero,'completada':ids.completada,'incompletos':incompletos})    
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
    except Exception, e:
        return render(request, 'base/error_no_encontrado.html')

def nance_editar(request, codi, num):
    str(codi)
    if request.user.is_superuser==1:
        try:
            ids = fichas.objects.get(cod_expediente=codi, numero=num)
            nanceFormSet = modelformset_factory(nance_tablas, nance_tabla, extra=0)
            nanceFormSet2 = modelformset_factory(nance_tablas, nance_tabla, extra=0)
            max_numero=10
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
                nance_general1 = nance_general.objects.get(fichas_id=ids.id)
                if request.method == 'GET':
                    form1 = nance_generalForm(instance=nance_general1)
                    formset = nanceFormSet(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
                    formset2 = nanceFormSet2(queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=2),prefix='2tablas')
                else:
                    form1 = nance_generalForm(request.POST, instance=nance_general1)
                    formset = nanceFormSet(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=1),prefix='1tablas')
                    formset2 = nanceFormSet2(request.POST, request.FILES, queryset=nance_tablas.objects.filter(fichas_id=ids.id,tabla=2),prefix='2tablas')
                    if (form1.is_valid() and formset.is_valid() and formset2.is_valid()):
                        form1.save()
                        for form in formset:
                            form.save()
                        for form in formset2:
                               form.save()
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                        return redirect('/analisis_denticion_mixta/moyersinferior/editar/%s/%s/' %(codi,num))
                    else: 
                        return render(request, 'AnalisisDenticionMixta/analisis_nance_editar.html', {'form1':form1,'formset':formset,'formset2':formset2,'codi':codi,'num':num,'max':max_numero,'ids':ids.id,'incompletos':incompletos})   
                return render(request, 'AnalisisDenticionMixta/analisis_nance_editar.html', {'form1':form1,'formset':formset,'formset2':formset2,'codi':codi,'num':num,'max':max_numero,'ids':ids.id,'incompletos':incompletos})   
            return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
        except Exception, e:
            if int(num)>1:
                return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
            else:
                return render(request, 'base/error_no_encontrado.html') 
    else:
        return render(request, 'base/error_no_hay_acceso.html')
################################################################################################################


def moyerssup_view(request,codi,num):
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
        if moyers_superior.objects.filter(fichas_id=ids.id).exists():
            genero = datos_generales.objects.get(cod_expediente=codi)
            moyerssupFormSet = modelformset_factory(moyers_superior_ancho, moyersSupAncForm, extra=0)
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
                    fecha =  timezone.now()
                    ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                    return redirect('/diag_general/nuevo/%s/%s' % (codi, num))
            return render(request, 'AnalisisDenticionMixta/moyerssuperior2.html', {'form1':form1,'formset':formset,'num':num,'codi':codi,'ids':ids.id,'genero':genero.genero,'incompletos':incompletos})
        else:
            if ids:
                max_num=4
                moyerssupFormSet = formset_factory(moyersSupAncForm, extra=4, max_num=4)
                if request.method == 'POST':
                    form1 = moyersSupForm(request.POST,initial={'fichas':ids.id})
                    formset = moyerssupFormSet(request.POST)
                    if (form1.is_valid() and formset.is_valid()):
                        form1.save()
                        for form in formset:
                            form.save()
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                        return redirect('/diag_general/nuevo/%s/%s' % (codi, num))
                    return render(request, 'AnalisisDenticionMixta/moyerssuperior.html', {'form1':form1, 'formset':formset, 'num':num,'codi':codi,'ids':ids.id,'max':max_num,'genero':genero.genero,'incompletos':incompletos})
                else:
                    form1 = moyersSupForm(initial={'fichas':ids.id})
                    formset = moyerssupFormSet()
                    genero = datos_generales.objects.get(cod_expediente=codi)
                    return render(request, 'AnalisisDenticionMixta/moyerssuperior.html', {'form1':form1, 'formset':formset, 'num':num,'codi':codi,'ids':ids.id,'max':max_num,'genero':genero.genero,'incompletos':incompletos})
    except Exception, e:
        if int(num)>1:
            return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
        else:
            return render(request, 'base/error_no_encontrado.html') 

def moyerssup_editar(request, codi, num):
    str(codi)
    if request.user.is_superuser==1:
        try:
            ids = fichas.objects.get(cod_expediente=codi, numero=num)
            genero = datos_generales.objects.get(cod_expediente=codi)
            moyerssupFormSet = modelformset_factory(moyers_superior_ancho, moyersSupAncForm, extra=0)
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
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                        return redirect('/diag_general/editar/%s/%s' % (codi, num))
                return render(request, 'AnalisisDenticionMixta/moyerssuperior_editar.html', {'form1':form1,'formset':formset,'num':num,'codi':codi,'ids':ids.id,'genero':genero.genero})  
            return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
        except Exception, e:
            if int(num)>1:
                return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
            else:
                return render(request, 'base/error_no_encontrado.html') 
    else:
        return render(request, 'base/error_no_hay_acceso.html')

def moyerssup_consultar(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        genero = datos_generales.objects.get(cod_expediente=codi)
        moyerssupFormSet = modelformset_factory(moyers_superior_ancho, moyersSupAncForm_consultar, extra=0)
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
            moysup = moyers_superior.objects.get(fichas_id=ids.id)
            if request.method == 'GET':
                form1 = moyersSupForm_consultar(instance=moysup)
                formset = moyerssupFormSet(queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
            else:
                form1 = moyersSupForm(request.POST, instance=moysup)
                formset = moyerssupFormSet(request.POST, request.FILES, queryset=moyers_superior_ancho.objects.filter(fichas_id=ids.id))
                    
                return redirect('/diag_general/consultar/%s/%s' % (codi, num))
            return render(request, 'AnalisisDenticionMixta/moyerssuperior_consultar.html', {'form1':form1,'formset':formset,'num':num,'codi':codi,'ids':ids.id,'genero':genero.genero,'completada':ids.completada,'incompletos':incompletos})    
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
    except Exception, e:
        return render(request, 'base/error_no_encontrado.html')


def moyersinf_view(request, codi, num):
    str(codi)
    try:
        ids = fichas.objects.get(cod_expediente=codi, numero=num,usuario_creador=request.user.id,completada=0)
        genero = datos_generales.objects.get(cod_expediente=codi)
        max_num = 4
        moyersinfFormSet = modelformset_factory(moyers_inferior_ancho, moyersInfAncForm, extra=0)
        incompletos =list()
        ficha = fichas.objects.filter(cod_expediente=codi,numero=num)
        for fi in ficha:
            if not registro.objects.filter(fichas_id=fi.id).exists():
                    incompletos.append(-1)
                    incompletos.append(-2)
                    incompletos.append(-3)        
        if moyers_inferior.objects.filter(fichas_id=ids.id).exists():
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
                    fecha =  timezone.now()
                    ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                    return redirect('/analisis_denticion_mixta/moyerssuperior/nuevo/%s/%s/' %(codi,num))
            return render(request, 'AnalisisDenticionMixta/moyersinferior2.html',{'form1': form1, 'formset': formset, 'codi': codi,'num':num, 'ids': ids.id,'genero':genero.genero,'incompletos':incompletos})
        else:
            if ids:
                max_num = 4
                moyersinfFormSet = formset_factory(moyersInfAncForm, extra=4, max_num=4)
                if request.method == 'POST':
                    form1 = moyersInfForm(request.POST, initial={'fichas': ids.id})
                    formset = moyersinfFormSet(request.POST)
                    if (form1.is_valid() and formset.is_valid()):
                        form1.save()
                        for form in formset:
                            form.save()
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                    return redirect('/analisis_denticion_mixta/moyerssuperior/nuevo/%s/%s/' %(codi,num))
                else:
                    form1 = moyersInfForm(initial={'fichas': ids.id})
                    formset = moyersinfFormSet()
            return render(request, 'AnalisisDenticionMixta/moyersinferior.html',{'form1': form1, 'formset': formset, 'codi': codi, 'ids': ids.id, 'num':num,'max': max_num,'genero':genero.genero,'incompletos':incompletos})
    except Exception, e:
        if int(num)>1:
            return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
        else:
            return render(request, 'base/error_no_encontrado.html') 


def moyersinf_editar(request, codi, num):
    str(codi)
    if request.user.is_superuser==1:
        try:
            genero = datos_generales.objects.get(cod_expediente=codi)
            ids = fichas.objects.get(cod_expediente=codi, numero=num)
            moyersinfFormSet = modelformset_factory(moyers_inferior_ancho, moyersInfAncForm, extra=0)
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
                moyinf = moyers_inferior.objects.get(fichas_id=ids.id)
                if request.method == 'GET':
                    print moyinf
                    form1 = moyersInfForm(instance=moyinf)
                    formset = moyersinfFormSet(queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
                else:
                    form1 = moyersInfForm(request.POST, instance=moyinf)
                    formset = moyersinfFormSet(request.POST, request.FILES,
                                               queryset=moyers_inferior_ancho.objects.filter(fichas_id=ids.id))
                    if form1.is_valid() and formset.is_valid():
                        form1.save()
                        formset.save()
                        fecha =  timezone.now()
                        ultima_modificacion.objects.filter(fichas_id=ids.id).update(fecha=fecha)
                        return redirect('/analisis_denticion_mixta/moyerssuperior/editar/%s/%s/' %(codi,num))
                return render(request, 'AnalisisDenticionMixta/moyersinferior_editar.html',{'form1': form1, 'formset': formset, 'codi': codi,'num':num, 'ids': ids.id,'genero':genero.genero})
            return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
        except Exception, e:
            if int(num)>1:
                return render(request, 'base/error_no_existe.html', {'num':int(num)-1})
            else:
                return render(request, 'base/error_no_encontrado.html') 
    else:
        return render(request, 'base/error_no_hay_acceso.html')

def moyersinf_consultar(request, codi, num):
    str(codi)
    try:
        genero = datos_generales.objects.get(cod_expediente=codi)
        ids = fichas.objects.get(cod_expediente=codi, numero=num)
        moyersinfFormSet = modelformset_factory(moyers_inferior_ancho, moyersInfAncForm_consultar, extra=0)
        if ids:
            moyinf = moyers_inferior.objects.get(fichas_id=ids.id)
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
            return render(request, 'AnalisisDenticionMixta/moyersinferior_consultar.html',{'form1': form1, 'formset': formset, 'codi': codi,'num':num, 'ids': ids.id,'genero':genero.genero,'completada':ids.completada,'incompletos':incompletos})
        return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha.")
    except Exception, e:
        return render(request, 'base/error_no_encontrado.html')
