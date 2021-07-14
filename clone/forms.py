from django.forms import fields,ModelForm
from .models import *
from django import forms
class NewImageForm(ModelForm):
    class Meta: 
        model=Image
        fields=[
            'image', 
            'caption',
            
        ]
       
        widget= {
            # 'image': forms.ImageField(attrs={
            #     'class': 'form-control',
            # }),
            # 'caption': forms.Textarea(attrs={
            #     'class': 'form-control',
            # })
          

            
        }