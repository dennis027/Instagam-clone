from .models import Image 
from django import forms
class NewImageForm(forms.ModelForm):
    class Meta:
        models= Image
        exclude = ['poster']
        widgets={
            ''
        }