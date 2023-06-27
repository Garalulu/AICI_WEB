from django import forms
from .models import VOCTB

class VOCForm(forms.ModelForm):
    class Meta:
        model = VOCTB
        fileds = {'voc_desc', 'voc_file',}