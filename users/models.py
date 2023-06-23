from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class UidTB(models.Model):
    uid = models.CharField(_("engineer identification number"), primary_key=True, unique=True, max_length=30) 
    name = models.CharField(_("engineer name"), max_length=30)
    
    def __str__(self):
        return self.uid

class EngineerTB(AbstractBaseUser, PermissionsMixin):
    usr_id = models.CharField(_("engineer ID"), unique=True, max_length=30)
    uid = models.ForeignKey(UidTB, on_delete=models.CASCADE)
    name = models.CharField(_("engineer name"), max_length=30)
    phonenum = models.CharField(_("engineer phone number"), max_length=11)
    is_staff = models.BooleanField(_("verify a staff"), default=False)
    is_active = models.BooleanField(_("verify a engineer active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    date_modified = models.DateTimeField(_("date modified"), auto_now=True)

    USERNAME_FIELD = "usr_id"
    REQUIRED_FIELDS = ["uid", "name", "phonenum"]

    objects = CustomUserManager()

    def __str__(self):
        return self.usr_id
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True