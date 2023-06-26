from django import forms
from .models import BoardTB

class BoardForm(forms.ModelForm):
    class Meta:
        model = BoardTB
        fields = ('usr_id', 'brd_title', 'brd_content')
