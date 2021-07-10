from django.forms import fields,ModelForm
from .models import *
from django import forms
class NewImageForm(ModelForm):
    class Meta: 
        models=Image
        fields=[
            'first name'
        ]
       
        widget= {
            'name': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }