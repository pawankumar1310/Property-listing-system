from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from . models import Apartment_Type, Property, Property_Detail

class PropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['title','address','city','pincode','state','upload']
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control'}),
		'address': forms.TextInput(attrs={'class': 'form-control'}),
		'city': forms.TextInput(attrs={'class': 'form-control'}),
		'pincode': forms.TextInput(attrs={'class': 'form-control'}),
		'state': forms.TextInput(attrs={'class': 'form-control'}),
		}

class PropertyDetailForm(forms.ModelForm):
	class Meta:
		model = Property_Detail
		fields = ['property','apartment_type','description','price','picture','sqft']

class ApartmentTypeForm(forms.ModelForm):
	class Meta:
		model = Apartment_Type
		fields = ['name']


