	# -*- coding: utf-8 -*-
from django import forms
from app.citas.models import *
from app.informacion.models import *

class citasForm(forms.ModelForm):
	class Meta:
		model = citas

		fields = [
		'fichas',
		'num_cita',
		'fecha_cita',
		'observaciones',
		'proxima_cita',
		'resultados',
		'autorizacion',
		'tutor',
		]

		labels={
		'fichas': 'Codigo Expediente',
		'num_cita':'N° de Cita',
		'fecha_cita':'Fecha de Cita',
		'observaciones':'Observaciones',
		'proxima_cita':'Fecha de proxima cita',
		'resultados':'Resultados Esperados',
		'autorizacion':'Autorización del Tutor',
		'tutor':'Tutor',
		}

		widgets = {
		'fichas':forms.TextInput(attrs={'class':'form-control'}),
		'num_cita':forms.TextInput(attrs={'class':'form-control'}),
		'fecha_cita':forms.DateInput(attrs={'class':'form-control'}),
		'observaciones':forms.Textarea(attrs={'class':'form-control'}),
		'proxima_cita':forms.DateInput(attrs={'class':'form-control'}),
		'resultados':forms.Textarea(attrs={'class':'form-control'}),
		'autorizacion':forms.CheckboxInput(attrs={'class':''}),
		'tutor':forms.TextInput(attrs={'class':'form-control'}),

		}

class citasForm2(forms.ModelForm):
	class Meta:
		model = citas

		fields = [
		'fichas',
		'num_cita',
		'fecha_cita',
		'observaciones',
		'proxima_cita',
		'resultados',
		'autorizacion',
		'tutor',
		]

		labels={
		'fichas': 'Codigo Expediente',
		'num_cita':'N° de Cita',
		'fecha_cita':'Fecha de Cita',
		'observaciones':'Observaciones',
		'proxima_cita':'Fecha de proxima cita',
		'resultados':'Resultados Esperados',
		'autorizacion':'Autorización del Tutor',
		'tutor':'Tutor',
		}

		widgets = {
		'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
		'num_cita':forms.HiddenInput(attrs={'class':'form-control'}),
		'fecha_cita':forms.DateInput(attrs={'class':'form-control'}),
		'observaciones':forms.TextInput(attrs={'class':'form-control'}),
		'proxima_cita':forms.DateInput(attrs={'class':'form-control'}),
		'resultados':forms.TextInput(attrs={'class':'form-control'}),
		'autorizacion':forms.CheckboxInput(attrs={'class':''}),
		'tutor':forms.TextInput(attrs={'class':'form-control'}),

		}

class citasGeneralesForm(forms.ModelForm):
	class Meta:
		model = citas_general

		fields = [
		'fichas',
		'aparato',
		'mx',
		'md',
		'estudiante',
		]

		labels={
		'fichas': 'Codigo Expediente',
		'aparato':'Aparato',
		'mx':'Maxilar (Mx)',
		'md':'Mandibular (Md)',
		'estudiante':'Estudiante',
		}
		widgets = {
		'fichas':forms.TextInput(attrs={'class':'form-control'}),
		'aparato':forms.TextInput(attrs={'class':'form-control','readonly':True}),
		'mx':forms.CheckboxInput(attrs={'class':''}),
		'md':forms.CheckboxInput(attrs={'class':''}),
		'estudiante':forms.HiddenInput(attrs={'class':'form-control'}),

		}

class citasGeneralesForm2(forms.ModelForm):
	class Meta:
		model = citas_general

		fields = [
		'fichas',
		'aparato',
		'mx',
		'md',
		'estudiante',
		]

		labels={
		'fichas': 'Codigo Expediente',
		'aparato':'Aparato',
		'mx':'Maxilar (Mx)',
		'md':'Mandibular (Md)',
		'estudiante':'Estudiante',
		}
		widgets = {
		'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
		'aparato':forms.Select(attrs={'class':'form-control','id':'id_aparato2'}),
		'mx':forms.CheckboxInput(attrs={'class':''}),
		'md':forms.CheckboxInput(attrs={'class':''}),
		'estudiante':forms.HiddenInput(attrs={'class':'form-control'}),

		}