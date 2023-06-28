from django import forms

from .models import ConstructionCallTB


class ConstructionCallForm(forms.ModelForm):
    class Meta:
        model = ConstructionCallTB
        fields = {'cstr_desc', 'cstr_file',}
        