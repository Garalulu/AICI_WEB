from django import forms

from .models import VOCTB


class VOCForm(forms.ModelForm):
    class Meta:
        model = VOCTB
        fields = {
            "voc_desc",
            "voc_file",
        }
