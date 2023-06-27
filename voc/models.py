from django.db import models
from django.utils.translation import gettext_lazy as _
import os


## Engineer working position
## cent_name
class CenterTB(models.Model):
    cent_name = models.CharField(_("center name"), unique=True, max_length=10)

    def __str__(self):
        return self.cent_name

## VOC
## cent_id
## voc_file        
class VOCTB(models.Model):
    cent = models.ForeignKey(CenterTB, on_delete=models.CASCADE, blank=True)
    # returns a string(>=1 char(s)) or a empty string('', with len()==0)
    # at first it hasn't any value, will get center position after data cleaning
    voc_desc = models.CharField(_("file name"), max_length=255, blank=True) 
    voc_file = models.FileField(_("uploaded file"), upload_to="voc/%Y/%m/%d")
    uploaded_at = models.DateTimeField(_("date uploaded"), auto_now_add=True)
    
    def get_filename(self):
        return os.path.basename(self.voc_file.name)


## Customer VOC information
#### Pre-TM list
## voc_id
## receipt
## cust_name
## declaration
## cust_type
## cust_nm
## cust_ads

#### After-TM list
## cust_importance
## is_tm
## is_answser
## tm_result
## tm_judge
class CustomerTB(models.Model):
    voc = models.ForeignKey(VOCTB, on_delete=models.CASCADE)
    receipt = models.DateTimeField(_("date joined"))
    cust_name = models.CharField(_("customer name"), max_length=30)
    declaration = models.CharField(_("additional info"), max_length=300)
    cust_num = models.CharField(_("customer phone number"), max_length=11)
    cust_ads = models.CharField(_("customer address"), max_length=30)
    
    cust_importance = models.BooleanField(_("customer level. 0: normal, 1: emergency"), default=0)
    is_tm = models.BooleanField(_("check TM status"), default=False)
    is_answer = models.BooleanField(_("check TM answer"))
    tm_result = models.BooleanField(_("check TM result"))
    tm_judge = models.CharField(_("TM messages"), max_length=50)
    
