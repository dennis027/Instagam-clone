from django.forms import fields,ModelForm
from .models import *
from django import forms
class NewImageForm(ModelForm):
    class Meta: 
        model=Poster
        fields=[
            'first_name'
        ]
       
        widget= {
            'name': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }