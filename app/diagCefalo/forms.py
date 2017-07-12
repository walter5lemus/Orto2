# -*- coding: utf-8 -*-
from django import forms
from app.diagCefalo.models import diagnostico_cefalometrico
from app.informacion.models import fichas


class diagCefaloForm(forms.ModelForm):

	class Meta:
		model = diagnostico_cefalometrico

		fields = [
			'fichas',
			'patron_esqueletal', 
			'otro_patron',
			'tipo_de_crecimiento',
			'medidas_dentales',
			'medidas_esteticas',

		]

		labels = {
			'fichas': 'Numero de Ficha',
			'patron_esqueletal': "Patrón Esqueletal",
			'otro_patron': "Otros:", 
			'tipo_de_crecimiento': "Tipo de Crecimiento",
			'medidas_dentales': "Medidas Dentales",
			'medidas_esteticas': "Medidas Estéticas",
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'patron_esqueletal': forms.Select(attrs={'class':'form-control'}),
			'otro_patron':forms.TextInput(attrs={'class':'form-control'}),
			'tipo_de_crecimiento':forms.Select(attrs={'class':'form-control'}),
			'medidas_dentales':forms.Select(attrs={'class':'form-control'}),
			'medidas_esteticas':forms.Textarea(attrs={'class':'form-control', 'rows':4}),
		}



class diagCefaloForm_consultar(forms.ModelForm):

	class Meta:
		model = diagnostico_cefalometrico

		fields = [
			'fichas',
			'patron_esqueletal', 
			'otro_patron',
			'tipo_de_crecimiento',
			'medidas_dentales',
			'medidas_esteticas',
		]

		labels = {
			'fichas': 'Numero de Ficha',
			'patron_esqueletal': "Patrón Esqueletal",
			'otro_patron': "Otros:", 
			'tipo_de_crecimiento': "Tipo de Crecimiento",
			'medidas_dentales': "Medidas Dentales",
			'medidas_esteticas': "Medidas Estéticas",
		}

		widgets = {
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'patron_esqueletal': forms.Select(attrs={'class':'form-control','readonly':True}),
			'otro_patron':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tipo_de_crecimiento':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'medidas_dentales':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'medidas_esteticas':forms.Textarea(attrs={'class':'form-control', 'rows':4,'readonly':True}),
		}