from django.db import models
from django.utils.translation import gettext_lazy as _

from voc.models import CenterTB


class ConstructionCallTB(models.Model):
    cent = models.ForeignKey(CenterTB, on_delete=models.CASCADE)
    cstr_desc = models.CharField(_("file name"), max_length=20) 
    cstr_file = models.FileField(_("uploaded file"), upload_to="construction/%Y/%m/%d")
    started_at = models.DateTimeField(_("construction date"), auto_now_add=True)

class ConstructionTB(models.Model):
    receipt = models.DateTimeField(_("date added"), auto_now_add=True)
    cstr_location = models.CharField(_("construction location"), max_length=30, blank=True)
    cstr_company = models.CharField(_("construction company"), max_length=30, blank=True)
    cstr_num = models.CharField(_("company tel number"), max_length=11, blank=True)   
    cstrcall = models.ForeignKey(ConstructionCallTB, on_delete=models.CASCADE)
