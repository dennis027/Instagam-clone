from .models import *
from django import forms
class NewImageForm(forms.ModelForm):
    class Meta: 
        models=models.ForeignKey(Image)
        your_name = forms.CharField(label='First Name',max_length=30)
        email = forms.EmailField(label='Email')
