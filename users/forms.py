from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import EngineerTB


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = EngineerTB
        fields = ("usr_id", "uid", "name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = EngineerTB
        fields = ("usr_id", "password", "uid", "name", "is_active", "is_staff")
