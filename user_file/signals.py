from django.db.models.signals import pre_delete
from django.dispatch import receiver

from user_file.models import UploadFile


@receiver(pre_delete, sender=UploadFile)
def pre_delete_upload_file(sender, instance, **kwargs):
    instance.file.delete()
