from django import forms

from .models import ConstructionCallTB


class ConstructionCallForm(forms.ModelForm):
    class Meta:
        model = ConstructionCallTB
        fields = {"cent", "cstr_file", "cstr_manager", "cstr_num"}
