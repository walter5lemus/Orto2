from django import forms
from app.diagCefalo.models import diagnostico_cefalometrico
from app.informacion.models import fichas


class diagCefaloForm(forms.ModelForm):

	class Meta:
		model = diagnostico_cefalometrico

		fields = [
			#'cod_expediente',
			'fichas',

			'patron_esqueletal', 
			'tipo_de_crecimiento',
			'medidas_dentales',
			'medidas_esteticas',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'patron_esqueletal': "Patron Esqueletal", 
			'tipo_de_crecimiento': "Tipo de Crecimiento",
			'medidas_dentales': "Medidas Dentales",
			'medidas_esteticas': "Medidas Esteticas",
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'patron_esqueletal':forms.Textarea(attrs={'class':'form-control'}),
			'tipo_de_crecimiento':forms.Textarea(attrs={'class':'form-control'}),
			'medidas_dentales':forms.Textarea(attrs={'class':'form-control'}),
			'medidas_esteticas':forms.Textarea(attrs={'class':'form-control'}),
		}



class diagCefaloForm_consultar(forms.ModelForm):

	class Meta:
		model = diagnostico_cefalometrico

		fields = [
			#'cod_expediente',
			'fichas',

			'patron_esqueletal', 
			'tipo_de_crecimiento',
			'medidas_dentales',
			'medidas_esteticas',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'patron_esqueletal': "Patron Esqueletal", 
			'tipo_de_crecimiento': "Tipo de Crecimiento",
			'medidas_dentales': "Medidas Dentales",
			'medidas_esteticas': "Medidas Esteticas",
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'patron_esqueletal': forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'tipo_de_crecimiento':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'medidas_dentales':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'medidas_esteticas':forms.Textarea(attrs={'class':'form-control','readonly':True}),
		}