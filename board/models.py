from django.db import models
from users.models import EngineerTB
from django.utils.translation import gettext_lazy as _

class BoardTB(models.Model):
    brd_id = models.AutoField(primary_key=True)
    engineer = models.ForeignKey(EngineerTB, on_delete=models.CASCADE)
    brd_title = models.CharField(_("게시판 제목"), max_length=200)
    brd_content = models.TextField(_("게시판 내용"))
    brd_create = models.DateTimeField(auto_now_add=True)
    brd_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.brd_id)
    
class UploadFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    brd_id = models.ForeignKey(BoardTB, on_delete=models.CASCADE)
    file = models.FileField(_("uploaded file"), upload_to="board/%Y/%m/%d",blank=True, null=True)
    
    def __str__(self):
        return str(self.file_id)
