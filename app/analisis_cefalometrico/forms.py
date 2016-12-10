# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from app.analisis_cefalometrico.models import *

class analisis_cefalometricoForm(forms.ModelForm):
	class Meta:
		model = analisis_cefalometrico

		fields = [	
			'fichas',
			'numero_de_examen',
			'sna',
			'snb',
			'anb',
			'convexidad',
			'wits',
			'long_cuerpo_mandibular',
			'profundidad_maxilar',
			'profundidad_facial',
			'plano_mandibular',
			'eje_y_fh',
			'cono_facial',
			'eje_facial',
			'angulo_goniaco_superior',
			'angulo_goniaco_inferior',
			'angulo_goniaco_total',
			'is_na',
			'is_sn',
			'isfh',
			'impa',
			'protusion_de_incisivo_max',
			'protusion_de_incisivo_md',
			'protusion_labial',
		]

		labels = {
			'fichas': 'Numero de ficha',
			'numero_de_examen': 'Numero de examen',
			'sna': 'SNA',
			'snb': 'SNB',
			'anb': 'ANB',
			'convexidad': 'Convexidad',
			'wits': 'Wits',
			'long_cuerpo_mandibular': 'Longitud del cuerpo mandibular',
			'profundidad_maxilar': 'Profundidad maxiliar',
			'profundidad_facial': 'Profundidad facial',
			'plano_mandibular': 'Plano mandibular',
			'eje_y_fh': 'Eje Y-FH',
			'cono_facial': 'Cono facial',
			'eje_facial': 'Eje facial',
			'angulo_goniaco_superior': 'Ángulo goniaco superior',
			'angulo_goniaco_inferior': 'Ángulo goniaco inferior',
			'angulo_goniaco_total': 'Ángulo goniaco total',
			'is_na': 'IS - NA',
			'is_sn': 'IS - NS',
			'isfh': 'ISFH',
			'impa': 'IMPA',
			'protusion_de_incisivo_max': 'Protusión de incisivo Mx',
			'protusion_de_incisivo_md': 'Protusión de incisivo Md',
			'protusion_labial': 'Protusión labial',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'numero_de_examen': forms.HiddenInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'sna': forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'snb': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'anb': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'convexidad': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'wits': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'long_cuerpo_mandibular': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'profundidad_maxilar': forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'profundidad_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'plano_mandibular': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'eje_y_fh': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'cono_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'eje_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'angulo_goniaco_superior': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'angulo_goniaco_inferior': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'angulo_goniaco_total': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'is_na': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'is_sn': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'isfh': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'impa': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'protusion_de_incisivo_max': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'protusion_de_incisivo_md': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'protusion_labial': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números'}),
		}


class analisis_cefalometricoForm_consultar(forms.ModelForm):
	class Meta:
		model = analisis_cefalometrico

		fields = [	
			'fichas',
			'numero_de_examen',
			'sna',
			'snb',
			'anb',
			'convexidad',
			'wits',
			'long_cuerpo_mandibular',
			'profundidad_maxilar',
			'profundidad_facial',
			'plano_mandibular',
			'eje_y_fh',
			'cono_facial',
			'eje_facial',
			'angulo_goniaco_superior',
			'angulo_goniaco_inferior',
			'angulo_goniaco_total',
			'is_na',
			'is_sn',
			'isfh',
			'impa',
			'protusion_de_incisivo_max',
			'protusion_de_incisivo_md',
			'protusion_labial',
		]

		labels = {
			'fichas': 'Numero de ficha',
			'numero_de_examen': 'Numero de examen',
			'sna': 'SNA',
			'snb': 'SNB',
			'anb': 'ANB',
			'convexidad': 'Convexidad',
			'wits': 'Wits',
			'long_cuerpo_mandibular': 'Longitud del cuerpo mandibular',
			'profundidad_maxilar': 'Profundidad maxiliar',
			'profundidad_facial': 'Profundidad facial',
			'plano_mandibular': 'Plano mandibular',
			'eje_y_fh': 'Eje Y-FH',
			'cono_facial': 'Cono facial',
			'eje_facial': 'Eje facial',
			'angulo_goniaco_superior': 'Ángulo goniaco superior',
			'angulo_goniaco_inferior': 'Ángulo goniaco inferior',
			'angulo_goniaco_total': 'Ángulo goniaco total',
			'is_na': 'IS - NA',
			'is_sn': 'IS - NS',
			'isfh': 'ISFH',
			'impa': 'IMPA',
			'protusion_de_incisivo_max': 'Protusión de incisivo Mx',
			'protusion_de_incisivo_md': 'Protusión de incisivo Md',
			'protusion_labial': 'Protusión labial',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
			'numero_de_examen': forms.HiddenInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números'}),
			'sna': forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'snb': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'anb': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'convexidad': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'wits': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'long_cuerpo_mandibular': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'profundidad_maxilar': forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'profundidad_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'plano_mandibular': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'eje_y_fh': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'cono_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'eje_facial': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'angulo_goniaco_superior': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'angulo_goniaco_inferior': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'angulo_goniaco_total': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'is_na': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'is_sn': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'isfh': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'impa': forms.NumberInput(attrs={'class':'form-control', 'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'protusion_de_incisivo_max': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'protusion_de_incisivo_md': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
			'protusion_labial': forms.NumberInput(attrs={'class':'form-control', 'step': 0.1,'pattern':'[0-9]{11}','title':'Solo se permiten números','readonly':True}),
		}