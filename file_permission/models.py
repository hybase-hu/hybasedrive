from django.contrib.auth.models import User
from django.db import models

from user_file.models import UploadFile


# Create your models here.
class UploadFilePermission(models.Model):
    file = models.ForeignKey(to=UploadFile,on_delete=models.CASCADE,related_name="all_permissions")
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="shared_with_me")
    created_at = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        unique_together = ('file', 'user')