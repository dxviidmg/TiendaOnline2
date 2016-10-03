#-*-encoding: utf-8 -*-
from django import forms
from .models import Orden
from django.utils.translation import ugettext_lazy as _

my_default_errors = {
    'required': 'Este campo es necesario',
    'invalid': 'Introduzca un dato valido'
	}

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model=Orden
		fields=[
			'nombre',
			'apellido',
			'email',
			'domicilio',
			'codigo_postal',
			'ciudad']
		labels={
			'nombre':_('Tu nombre'),
			'apellido':_('Apellido'),
			'domicilio':_('Direccion'),
			'codigo_postal':_('Codigo postal'),
			'ciudad':_('Ciudad')
		}
		error_messages = {
			'nombre': my_default_errors,
			'apellido': my_default_errors,
			'email': my_default_errors,
			'domicilio': my_default_errors,
			'codigo_postal': my_default_errors,
			'ciudad': my_default_errors
		}