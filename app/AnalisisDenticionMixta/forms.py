# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from app.AnalisisDenticionMixta.models import *

class nance_generalForm(forms.ModelForm):
    class Meta:
        model = nance_general

        fields = [
            'fichas',
            'ed_maxi',
            'ed_mand',
        ]

        labels={
            'fichas': 'Código Expediente y Numero de Ficha' ,
            'ed_maxi':'Espacio Disponible Maxilar M1-6 a M2-6',
            'ed_mand': 'Espacio Disponible Mandibular M4-6 a M3-6',
        }

        widgets={
            'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
            'ed_maxi': forms.NumberInput(attrs={'class':'form-control','min':0,'max': 2147483647}),
            'ed_mand': forms.NumberInput(attrs={'class':'form-control','min':0,'max': 2147483647}),
        }

class nance_generalForm_Consultar(forms.ModelForm):
    class Meta:
        model = nance_general

        fields = [
            'fichas',
            'ed_maxi',
            'ed_mand',
        ]

        labels={
            'fichas': 'Código Expediente y Numero de Ficha' ,
            'ed_maxi':'Espacio Disponible Maxilar M1-6 a M2-6',
            'ed_mand': 'Espacio Disponible Mandibular M4-6 a M3-6',
        }

        widgets={
            'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
            'ed_maxi': forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647}),
            'ed_mand': forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647}),
        }

class nance_tabla(forms.ModelForm):
    class Meta:
        model = nance_tablas

        fields = [
            'id',
            'seleccion',
            'fichas',
            'tabla',
            'posicion',
            'mdm',
            'mprx',
            'mdrx',
            'multiplicacion',
            'valor_x',
        ]

        labels={
            'id': '' ,
            'seleccion': '' ,
            'fichas':'',
            'tabla':'',
            'posicion':'',
            'mdm':'',
            'mprx':'',
            'mdrx':'',
            'multiplicacion':'',
            'valor_x':'',
        }

        widgets={
            'id':forms.HiddenInput(attrs={'class':'checkbox','readonly':True}),
            'seleccion':forms.CheckboxInput(attrs={'class':'checkbox','readonly':True}),
            'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
            'tabla':forms.HiddenInput(attrs={'class':'form-control'}),
            'posicion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'mdm':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647,'step':'0.01'}),
            'mprx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647,'step':'0.01'}),
            'mdrx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647,'step':'0.01'}),
            'multiplicacion':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0,'max': 2147483647,'step':'0.01'}),
            'valor_x':forms.NumberInput(attrs={'class':'form-control x','required':True,'min':0,'max': 2147483647,'step':'0.01'}),
        }

class nance_tabla_consultar(forms.ModelForm):
    class Meta:
        model = nance_tablas

        fields = [
            'seleccion',
            'fichas',
            'tabla',
            'posicion',
            'mdm',
            'mprx',
            'mdrx',
            'multiplicacion',
            'valor_x',
        ]

        labels={
            'seleccion': '' ,
            'fichas':'',
            'tabla':'',
            'posicion':'',
            'mdm':'',
            'mprx':'',
            'mdrx':'',
            'multiplicacion':'',
            'valor_x':'',
        }

        widgets={
            'seleccion':forms.CheckboxInput(attrs={'class':'checkbox','disabled':True}),
            'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
            'tabla':forms.HiddenInput(attrs={'class':'form-control'}),
            'posicion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'mdm':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0}),
            'mprx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0}),
            'mdrx':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0}),
            'multiplicacion':forms.NumberInput(attrs={'class':'form-control','readonly':True,'min':0}),
            'valor_x':forms.NumberInput(attrs={'class':'form-control x','readonly':True,'min':0}),
    }        


class moyersSupForm(forms.ModelForm):
    class Meta:
        model = moyers_superior

        fields = [  
            'fichas',
            'ed_izquierdo',
            'ed_derecho',       
        ]

        labels = {
            'fichas': 'Número de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
            'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'required':True}),
            'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'required':True}),
        }

class moyersSupAncForm(forms.ModelForm):
    class Meta:
        model = moyers_superior_ancho

        fields = [  
            'fichas',
            'posicion',
            'ancho_mesiodistal',        
        ]

        labels = {
            'fichas': 'Numero de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class':'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'max':15,'required':True}),
        }

class moyersSupForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_superior

        fields = [  
            'fichas',
            'ed_izquierdo',
            'ed_derecho',       
        ]

        labels = {
            'fichas': 'Número de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
            'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'readonly':True}),
            'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'readonly':True}),
            }

class moyersSupAncForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_superior_ancho

        fields = [  
            'fichas',
            'posicion',
            'ancho_mesiodistal',        
        ]

        labels = {
            'fichas': 'Número de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class':'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'max':15,'readonly':True}),
        }


class moyersInfForm(forms.ModelForm):
    class Meta:
        model = moyers_inferior

        fields = [
            'fichas',
            'ed_izquierdo',
            'ed_derecho',
        ]

        labels = {
            'fichas': 'Número de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'required':True}),
            'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'required':True}),
                   }


class moyersInfAncForm(forms.ModelForm):
    class Meta:
        model = moyers_inferior_ancho

        fields = [
            'fichas',
            'posicion',
            'ancho_mesiodistal',
        ]

        labels = {
            'fichas': 'Número de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'max':15,'required':True}),
        }


class moyersInfForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_inferior

        fields = [
            'fichas',
            'ed_izquierdo',
            'ed_derecho',
        ]

        labels = {
            'fichas': 'Número de ficha',
            'ed_izquierdo': 'Ed Izquierdo',
            'ed_derecho': 'Ed Derecho',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ed_izquierdo': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'readonly':True}),
            'ed_derecho': forms.NumberInput(attrs={'class':'form-control','min':1,'max':30,'readonly':True}),
        }


class moyersInfAncForm_consultar(forms.ModelForm):
    class Meta:
        model = moyers_inferior_ancho

        fields = [
            'fichas',
            'posicion',
            'ancho_mesiodistal',
        ]

        labels = {
            'fichas': 'Número de ficha',
            'posicion': 'Posición',
            'ancho_mesiodistal': 'Ancho Mesiodistal',
        }

        widgets = {
            'fichas': forms.HiddenInput(attrs={'class': 'form-control'}),
            'posicion': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ancho_mesiodistal': forms.NumberInput(attrs={'class':'form-control','min':1,'max':15,'readonly':True}),
        }
