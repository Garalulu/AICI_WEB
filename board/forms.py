from django import forms
from .models import BoardTB, UploadFile

class BoardForm(forms.ModelForm):
    class Meta:
        model = BoardTB
        fields = ['brd_title', 'brd_content']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']
