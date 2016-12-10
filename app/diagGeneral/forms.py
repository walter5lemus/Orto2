from django import forms
from app.aspMandibular.choices import *
from app.diagGeneral.models import diagnostico_general
from app.informacion.models import fichas


class diagGeneralForm(forms.ModelForm):

	class Meta:
		model = diagnostico_general

		fields = [
			#'cod_expediente',
			'fichas',

			'diagnostico_ortodontico_general', 
			'problemas',
			'objetivos',
			'tratamiento',
			'descripcion_tratamiento',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'diagnostico_ortodontico_general': "Diagnostico Ortodontico General", 
			'problemas': "Problemas",
			'objetivos': "Objetivos",
			'tratamiento': "Tratamiento",
			'descripcion_tratamiento': "Descripcion del Plan de Tratamiento",
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'diagnostico_ortodontico_general':forms.TextInput(attrs={'class':'form-control'}),
			'problemas':forms.TextInput(attrs={'class':'form-control'}),
			'objetivos':forms.TextInput(attrs={'class':'form-control'}),
			'tratamiento':forms.Select(attrs={'class':'form-control'}),
			'descripcion_tratamiento':forms.TextInput(attrs={'class':'form-control'}),
		}



class diagGeneralForm_consultar(forms.ModelForm):

	class Meta:
		model = diagnostico_general

		fields = [
			#'cod_expediente',
			'fichas',

			'diagnostico_ortodontico_general', 
			'problemas',
			'objetivos',
			'tratamiento',
			'descripcion_tratamiento',
		]

		labels = {
			#'cod_expediente': 'Codigo expediente',
			'fichas': 'Numero de Ficha',

			'diagnostico_ortodontico_general': "Diagnostico Ortodontico General", 
			'problemas': "Problemas",
			'objetivos': "Objetivos",
			'tratamiento': "Tratamiento",
			'descripcion_tratamiento': "Descripcion del Plan de Tratamiento",
		}

		widgets = {
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),

			'diagnostico_ortodontico_general':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'problemas':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'objetivos':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'tratamiento':forms.Select(attrs={'class':'form-control','readonly':True,'disabled':True}),
			'descripcion_tratamiento':forms.TextInput(attrs={'class':'form-control','readonly':True}),
		}
