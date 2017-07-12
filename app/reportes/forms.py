# -*- coding: utf-8 -*-
from django import forms
from app.reportes.models import *
from django.contrib.admin import widgets
#from app.informacion.choices import *

class reportesForms(forms.ModelForm):
	class Meta:
		model = reportes

		fields = [
			'fichas',
			'codigo',
			'numero',
		]

		labels={
			'fichas': 'Código Expediente y Numero de Ficha'	,
			'codigo':'Código',
			'numero':'Numero de Ficha',
		}

		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'codigo':forms.TextInput(attrs={'class':'form-control'}),
			'numero':forms.Select(attrs={'class':'form-control'}),
		}
