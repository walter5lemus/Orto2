# -*- coding: utf-8 -*-
from io import BytesIO
import copy
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect    
from reportlab.lib.pagesizes import letter, landscape
from django.core import serializers
from reportlab.platypus import *
from reportlab.lib.units import cm
from reportlab.lib.styles import *
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import *
from reportlab.pdfgen import canvas
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame    
)
from app.aspMandibular.choices import *
from app.informacion.models import *
from app.informacion.forms import *
from reportlab.lib import utils

from app.gestorImg.models import img_paciente, img_paciente2, img_radiograficas, img_modelo, img_aparato 


from app.diagCefalo.models import *
from app.diagGeneral.models import *
from app.reportes.models import *
from app.reportes.forms import *
#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
import time
import locale

# Establecemos el locale de nuestro sistema
locale.setlocale(locale.LC_ALL, "")
 


def reporte_crear(request):
    
    #user = request.user.id
    if request.method == 'POST':
        form = reportesForms(request.POST,initial={})
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('reportes:reporte_nuevo')
    else:

        form = DatosGeneralesForm()
    return render(request, 'reportes/reportes_nuevo.html', {'form':form})

def reporte_error(request):
    
    form = DatosGeneralesForm()
    return render(request, 'base/error_no_encontrado_reporte.html', {'form':form})

class BusquedaAjaxView(TemplateView):
    def get(self,request,*args,**kwargs):
        codigo = request.GET['codigo']
        cod = list(datos_generales.objects.filter(cod_expediente=codigo))
        data = serializers.serialize('json', cod)
        return HttpResponse(data, content_type='application/json')

class BusquedaAjaxView2(TemplateView):
    def get(self,request,*args,**kwargs):
        codigo = request.GET['codigo']
        try:
            fi=list(fichas.objects.filter(cod_expediente=codigo))
            data = serializers.serialize('json', fi, fields=('numero','completada'))
            return HttpResponse(data, content_type='application/json')
        except Exception, e:
            return HttpResponse('Error', status=401)


class ReportePersonasPDF(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
        if diagnostico_cefalometrico.objects.filter(fichas_id=ids.id).exists():
            if diagnostico_general.objects.filter(fichas_id=ids.id).exists():
                
                #Indicamos el tipo de contenido a devolver, en este caso un pdf
                response = HttpResponse(content_type='application/pdf')
                
                #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                buffer = BytesIO()
                #Canvas nos permite hacer el reporte con coordenadas X y Y
                pdf = canvas.Canvas(buffer)
                pdf.setTitle("Reporte Diagnostico_"+codigo+"_ficha="+numero+".pdf")
                pdf.pdf_name = "Reporte Diagnostico_"+codigo+"_ficha="+numero+".pdf"
                #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
                self.cabecera(pdf)
                self.cuerpo(pdf,codigo,numero)
                self.pie(pdf)
                #Con show page hacemos un corte de página para pasar a la siguiente
                pdf.showPage()
                pdf.save()
                pdf = buffer.getvalue()
                buffer.close()
                response.write(pdf)
                return response
        return HttpResponseRedirect('/reportes/error/')




    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 20, 750, 120, 90,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(200, 790, u"Universidad de El Salvador")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(220, 770, u"Facultad de Odontología")
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen2 = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen2, 460  , 750, 120, 90,preserveAspectRatio=True)
        pdf.line(20,740,580,740)
        #pdf.setStrokeColorRGB(0.0, 0.0, 2.46)  # Color de trazo

    def cuerpo(self,pdf,codigo,numero):
        #Primera parte del cuerpo
        pdf.drawString(50, 680, "N° de Expediente:")
        pdf.drawString(250, 680,codigo)
        p = datos_generales.objects.get(cod_expediente=codigo)
        pdf.drawString(50, 650, "Nombre:")
        pdf.drawString(250, 650,p.nombre_completo)
        pdf.drawString(50, 620, "Fecha de Nacimiento:")
        pdf.drawString(250, 620, "{:%d- %B- %Y}".format(p.fecha_nac))

        #Segunda parte del cuerpo
        ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
        diagCefalo =  diagnostico_cefalometrico.objects.get(fichas_id=ids.id)   
        diagGen =  diagnostico_general.objects.get(fichas_id=ids.id)
       
        pdf.drawString(50, 560, "Radiograficamente presenta:")
        pdf.drawString(80, 520, "Patron Esqueletal")
        pdf.drawString(250, 520, diagCefalo.get_patron_esqueletal_display())
        pdf.drawString(80, 480, "Tipo de Crecimiento")
        pdf.drawString(250, 480, diagCefalo.get_tipo_de_crecimiento_display())
        pdf.drawString(80, 440, "Medidas Dentales")
        pdf.drawString(250, 440, diagCefalo.get_medidas_dentales_display())
        pdf.drawString(80, 400, "Medidas Esteticas")
        pdf.drawString(250, 400, diagCefalo.medidas_esteticas)



        pdf.drawString(50, 340, "Clinicamente se Observa:")
        pdf.drawString(80, 300, "Diagnostico Ortodontico General")
        
        styles = getSampleStyleSheet()

        ParaStyle = copy.deepcopy(styles["Normal"])
        ParaStyle.spaceBefore = 0.2 * cm
        ParaStyle.alignment = TA_JUSTIFY
        ParaStyle.fontName = 'Helvetica'
        ParaStyle.fontSize = 14
        ParaStyle.leading = 15
        #ParaStyle.setFont("Helvetica", 14)
        p=Paragraph(diagGen.diagnostico_ortodontico_general, ParaStyle)
        p.wrapOn(pdf,460,500)
        p.drawOn(pdf, 2.85* cm, 7.6 * cm)

        pdf.drawString(50,150, "Se recomienda Tratamiento de:")
        #pdf.drawString(250, 150, dict(Tratamiento).get(diagGen.tratamiento))
        pdf.drawString(280, 150, diagGen.get_tratamiento_display())

    def pie(self,pdf):
        pdf.line(20,90,580,90)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(200, 70, u"Facultad de Odontología")    
        pdf.drawString(190, 58, u"Universidad de El Salvador")
        pdf.drawString(130, 46, u"Final 25 Av. Nte, Ciudad Universitaria, San Salvador")
        pdf.drawString(200, 34, u"Tels.: (503) 2225 7198")
        pdf.drawString(182, 20, u"www.odontología.ues.edu.sv")
        archivo_imagen3 = settings.MEDIA_ROOT+'/imagenes/logofb.jpg'
        pdf.drawImage(archivo_imagen3, 440 , 25, 40, 40,preserveAspectRatio=True)
        archivo_imagen4 = settings.MEDIA_ROOT+'/imagenes/logotw.jpg'
        pdf.drawImage(archivo_imagen4, 500 , 25, 40, 40,preserveAspectRatio=True)





#**********************************************************************************************

def generar_pdf_Caducar(request):
    fecha = time.strftime("%x")
    str(fecha)
    response = HttpResponse(content_type='application/pdf')

    pdf_name = "fichas_caducadas_"+fecha+".pdf"  # llamado producto
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=60,
                            bottomMargin=18,
                            )
    doc.title = "fichas_caducadas"
    clientes = []
    styles = getSampleStyleSheet()
    headerStyle = ParagraphStyle(
            name='Total',
            fontSize=18,
            fontName='Helvetica-BoldOblique',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_CENTER)
    headerStyle2 = ParagraphStyle(
            name='Total',
            fontSize=16,
            fontName='Helvetica-BoldOblique',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_CENTER)

    parrafoStyle = ParagraphStyle(
            name='Total1',
            fontSize=12,
            fontName='Helvetica',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_CENTER)

    fechaStyle = ParagraphStyle(
            name='Total1',
            fontSize=14,
            fontName='Helvetica',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_RIGHT)

    universidad= "UNIVERSIDAD DE EL SALVADOR"
    p1 = Paragraph(universidad, headerStyle)
    clientes.append(p1)

    facultad = "FACULTAD DE ODONTOLOGIA"
    p1 = Paragraph(facultad, headerStyle2)
    clientes.append(p1)

    image = Image(settings.MEDIA_ROOT+'/imagenes/logo.png', width=100, height=100)
    clientes.append(image)

    text= "FICHAS QUE SE CADUCARON"
    p1 = Paragraph(text, headerStyle)
    clientes.append(p1)
    tex= "\n"
    p1 = Paragraph(tex, headerStyle)
    clientes.append(p1) 

    headings = ('Codigo Expediente', 'N° de Ficha','Nombre Completo','Usuario Creador')
    allclientes = [(p.cod_expediente, p.numero, p.cod_expediente.nombre_completo,p.cod_expediente.usuario_creador) for p in fichas.objects.filter(completada=0)  ]


    t = Table([headings] + allclientes)
    t.setStyle(TableStyle( 
        [
            ('GRID', (0, 0), (4, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            #('ALIGN', (1,1), (-1,0), 'CENTER'),
        ],
    ))
    clientes.append(t)
    p1 = Paragraph(fecha,fechaStyle)
    clientes.append(p1)

    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response


class ReporteImagenes(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_paciente.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
                    
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_paciente.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        pfacial =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.pfacial)
        pdf.drawImage(pfacial, 50, 400, 175, 175)

        pfrontal =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.pfrontal)
        pdf.drawImage(pfrontal, 312, 400, 175, 175)

        psonrisa =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.psonrisa)
        pdf.drawImage(psonrisa, 575, 400, 175, 175)


#****************************** SEGUNDA FILA *******************************

        osuperior =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.osuperior)
        pdf.drawImage(osuperior, 25, 215, 225, 150)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 460, 310, 60, 60)

        pdf.drawString(275, 310, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(275, 290, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(275, 270, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(275, 250, 'FECHA DE NACIMIENTO: '+"{:%d-%B-%Y}".format(datos.fecha_nac))
        pdf.drawString(275, 230, 'ESTUDIANTE: '+imagen_paciente.userone)

        oinferior =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.oinferior)
        pdf.drawImage(oinferior, 550, 215, 225, 150)


#****************************** TERCERA FILA *******************************

        lizquierdo =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lizquierdo)
        pdf.drawImage(lizquierdo, 25, 25, 225, 150)

        frontal =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.frontal)
        pdf.drawImage(frontal, 290, 25, 225, 150)

        lderecho =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lderecho)
        pdf.drawImage(lderecho, 550, 25, 225, 150)



class ReporteImagenes2(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_paciente.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
                    
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_paciente2.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        pfacial =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.pfacial2)
        pdf.drawImage(pfacial, 50, 400, 175, 175)

        pfrontal =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.pfrontal2)
        pdf.drawImage(pfrontal, 312, 400, 175, 175)

        psonrisa =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.psonrisa2)
        pdf.drawImage(psonrisa, 575, 400, 175, 175)


#****************************** SEGUNDA FILA *******************************

        osuperior =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.osuperior2)
        pdf.drawImage(osuperior, 25, 215, 225, 150)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 460, 310, 60, 60)

        pdf.drawString(275, 310, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(275, 290, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(275, 270, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(275, 250, 'FECHA DE NACIMIENTO: '+"{:%d-%B-%Y}".format(datos.fecha_nac))
        pdf.drawString(275, 230, 'ESTUDIANTE: '+imagen_paciente.usertwo)

        oinferior =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.oinferior2)
        pdf.drawImage(oinferior, 550, 215, 225, 150)


#****************************** TERCERA FILA *******************************

        lizquierdo =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lizquierdo2)
        pdf.drawImage(lizquierdo, 25, 25, 225, 150)

        frontal =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.frontal2)
        pdf.drawImage(frontal, 290, 25, 225, 150)

        lderecho =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lderecho2)
        pdf.drawImage(lderecho, 550, 25, 225, 150)


class ReporteImagenes_Modelo(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_modelo.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
                    
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_Modelo_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Modelo_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_modelo.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        osupm =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.osupm)
        pdf.drawImage(osupm, 280, 410, 235, 175)

        oinfm =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.oinfm)
        pdf.drawImage(oinfm, 280, 30, 235, 175)

        lizqm =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lizqm)
        pdf.drawImage(lizqm, 25, 220, 235, 175)

        frontm =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.frontm)
        pdf.drawImage(frontm, 280, 220, 235, 175)

        lderm =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.lderm)
        pdf.drawImage(lderm, 535, 220, 235, 175)


#****************************** Datos Generales *******************************

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 700, 140, 60, 60)

        pdf.drawString(535, 140, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(535, 120, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(535, 100, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(535, 80, 'FECHA DE REGISTRO: '+"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        pdf.drawString(535, 60, 'ESTUDIANTE: '+imagen_paciente.userm)

class ReporteImagenes_Radiograficas_panoramica_inicial(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html')
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        ipano =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.ipano)
        pdf.drawImage(ipano, 25, 25, 745, 470)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 570, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 570, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(500, 570, 'FECHA DE REGISTRO: '+str(imagen_paciente.ifecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        pdf.drawString(25, 530, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 530, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 715, 520, 60, 60)


class ReporteImagenes_Radiograficas_panoramica_trazados(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        tpano =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.tpano)
        pdf.drawImage(tpano, 25, 25, 745, 470)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 570, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 570, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(500, 570, 'FECHA DE REGISTRO: '+str(imagen_paciente.tfecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        pdf.drawString(25, 530, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 530, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 715, 520, 60, 60)

class ReporteImagenes_Radiograficas_panoramica_seguimiento(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        spano =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.spano)
        pdf.drawImage(spano, 25, 25, 745, 470)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 570, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 570, 'PACIENTE: '+datos.nombre_completo)
        pdf.drawString(500, 570, 'FECHA DE REGISTRO: '+str(imagen_paciente.sfecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        pdf.drawString(25, 530, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 530, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 715, 520, 60, 60)

class ReporteImagenes_Radiograficas_cefalometrica_inicial(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer)
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        icefa =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.icefa)
        pdf.drawImage(icefa, 25, 25, 545, 650)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 790, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 790, 'PACIENTE: '+datos.nombre_completo)

        pdf.drawString(25, 750, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 750, 'FECHA DE REGISTRO: '+str(imagen_paciente.ifecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        
        pdf.drawString(25, 710, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 500, 730, 75, 75)

class ReporteImagenes_Radiograficas_cefalometrica_trazados(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer)
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        tcefa =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.tcefa)
        pdf.drawImage(tcefa, 25, 25, 545, 650)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 790, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 790, 'PACIENTE: '+datos.nombre_completo)

        pdf.drawString(25, 750, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 750, 'FECHA DE REGISTRO: '+str(imagen_paciente.tfecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        
        pdf.drawString(25, 710, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 500, 730, 75, 75)

class ReporteImagenes_Radiograficas_cefalometrica_seguimiento(View):

    def get(self,request, *args, **kwargs):
        codigo = self.kwargs['codigo']
        numero = self.kwargs['num']
        nombreUser = str(request.user.first_name) + " " + str(request.user.last_name)

        try:
            if fichas.objects.filter(cod_expediente=codigo, numero=numero).exists(): 
                ids = fichas.objects.get(cod_expediente=codigo, numero=numero)
                if img_radiograficas.objects.filter(fichas_id=ids.id).exists():
                    #Indicamos el tipo de contenido a devolver, en este caso un pdf
                    response = HttpResponse(content_type='application/pdf')
        
                    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                    buffer = BytesIO()
                    #Canvas nos permite hacer el reporte con coordenadas X y Y
                    pdf = canvas.Canvas(buffer)
                    pdf.setTitle("Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf")
                    pdf.pdf_name = "Reporte Imagenes_Radiograficas_"+codigo+"_ficha="+numero+".pdf"
                    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name


                    #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.s
                    self.cuerpo(pdf,codigo,numero)
                    #Con show page hacemos un corte de página para pasar a la siguiente
                    pdf.showPage()
                    pdf.save()
                    pdf = buffer.getvalue()
                    buffer.close()
                    response.write(pdf)
                    return response
                return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})
            return render(request, 'base/error_no_encontrado.html', {'nombreUser':nombreUser})
        except Exception as e:
            return render(request, 'base/error_no_encontrado_imagenes.html', {'nombreUser':nombreUser})

    def cuerpo(self,pdf,codigo,numero):
        datos =datos_generales.objects.get(cod_expediente=codigo)
        ids = fichas.objects.get(cod_expediente_id=codigo,numero=numero)
        imagen_paciente = img_radiograficas.objects.get(fichas_id=ids.id)
        pdf.setFont("Helvetica", 8)
#****************************** PRIMERA FILA *******************************
        scefa =  settings.MEDIA_ROOT+'/'+str(imagen_paciente.scefa)
        pdf.drawImage(scefa, 25, 25, 545, 650)

#****************************** Datos Generales *******************************

        pdf.drawString(25, 790, 'EXPEDIENTE: '+datos.cod_expediente+'  FICHA: '+numero)
        pdf.drawString(225, 790, 'PACIENTE: '+datos.nombre_completo)

        pdf.drawString(25, 750, 'EDAD: '+str(datos.edad)+' años')
        pdf.drawString(225, 750, 'FECHA DE REGISTRO: '+str(imagen_paciente.sfecha))#"{:%d-%B-%Y}".format(datos.fecha_hora_creacion))
        
        pdf.drawString(25, 710, 'ESTUDIANTE: '+imagen_paciente.user)

        logo_odontologia = settings.MEDIA_ROOT+'/imagenes/logo3.jpg'
        pdf.drawImage(logo_odontologia, 500, 730, 75, 75)
