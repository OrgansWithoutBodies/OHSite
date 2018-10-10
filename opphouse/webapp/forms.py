from django import forms

#https://docs.wagtail.io/en/v2.0/reference/contrib/forms/customisation.html for multistep wagtail forms
from .models import *

class CarForm(forms.ModelForm):
		#year make model next to each other w default values 
	class Meta:
		model=Car
		fields=['vin','mileage','year','make','carmodel','extrainfo']


class DonorForm(forms.ModelForm):
	class Meta:
		model=Donor
		fields='__all__'
		


class ContactForm(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	phone=forms.IntegerField()
	message=forms.CharField()