from django import forms
from django.forms import ModelForm
from .models import Repuestos

class RepuestosForm(ModelForm):

    class Meta:
        model = Repuestos
        fields =['id','serial','marca']
