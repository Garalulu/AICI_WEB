from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from voc.models import CenterTB

## KT API DB
class APITB(models.Model):
    key_count = models.IntegerField(_("KT API Callback Key"))

## Engineer identification number DB
## - uid
## - name
## - cent_id
class UidTB(models.Model):
    uid = models.CharField(_("engineer identification number"), primary_key=True, unique=True, max_length=30) 
    name = models.CharField(_("engineer name"), max_length=30)
    cent = models.ForeignKey(CenterTB, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.uid

## User DB
## - id: primary key. auto-created
## - password: auto-created
## - last_login: auto-created
## - is_superuser: auto-created
## - usr_id
## - name
## - phonenum
## - is_staff
## - is_active
## - date_joined
## - date_modified
## - uid_id: foreign key. UidTB's uid
class EngineerTB(AbstractBaseUser, PermissionsMixin):
    usr_id = models.CharField(_("engineer ID"), unique=True, max_length=30)
    uid = models.ForeignKey(UidTB, on_delete=models.CASCADE)
    name = models.CharField(_("engineer name"), max_length=30)
    # phonenum = models.CharField(_("engineer phone number"), max_length=11)
    is_staff = models.BooleanField(_("verify a staff"), default=False)
    is_active = models.BooleanField(_("verify a engineer active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    date_modified = models.DateTimeField(_("date modified"), auto_now=True)

    ## usr_id replaces username, which is default setting for Django AbstractBaseUser
    USERNAME_FIELD = "usr_id"
    ## User should fill below fields too when register
    REQUIRED_FIELDS = ["uid", "name"]

    ## Custom user manager for EngineerTB
    ## managers.py
    objects = CustomUserManager()

    def __str__(self):
        return self.usr_id
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True