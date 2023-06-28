from django import forms

from .models import ConstructionTB


class ConstructionForm(forms.ModelForm):
    class Meta:
        model = ConstructionTB
        fields = {'cstr_desc', 'cstr_file',}
        