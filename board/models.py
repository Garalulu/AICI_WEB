from django.db import models
from users.models import EngineerTB
from django.utils.translation import gettext_lazy as _

class BoardTB(models.Model):
    brd_id = models.CharField(_("board ID"), unique=True, max_length=30)
    usr_id = models.ForeignKey("users.EngineerTB", on_delete=models.CASCADE)
    brd_title = models.CharField(_("board title"), max_length=200)
    brd_content = models.TextField(_("board content"))
    brd_create = models.DateTimeField(auto_now_add=True)
    brd_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.brd_id