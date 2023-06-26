from django.db import models
from users.models import EngineerTB
from django.utils.translation import gettext_lazy as _

class BoardTB(models.Model):
    brd_id = models.AutoField(primary_key=True)  # 자동으로 증가하는 기본 키 필드
    usr_id = models.ForeignKey("users.EngineerTB", on_delete=models.CASCADE)
    brd_title = models.CharField(_("board title"), max_length=200)
    brd_content = models.TextField(_("board content"))
    brd_create = models.DateTimeField(auto_now_add=True)
    brd_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.brd_id)
