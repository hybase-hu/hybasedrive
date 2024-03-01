import os.path

from django.contrib.auth.models import User
from django.db import models

from hybasedrive.settings import BASE_DIR

# Create your models here.
FILE_TYPE = (
    ("0", "Directory"),
    ("1", "File")
)


def user_upload_to_path(instance, filename):
    return os.path.join("uploaded_files", instance.owner.username, filename)


class UploadFile(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name="my_files")
    file_type = models.CharField(choices=FILE_TYPE, max_length=1)
    file = models.FileField(upload_to=user_upload_to_path)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    description = models.TextField(blank=True, default="no description")

    def filename(self):
        return os.path.basename(self.file.name)

    def get_extension(self):
        name, extension = os.path.splitext(self.file.name)
        return str(extension)

    def file_type_image(self):
        extension = self.get_extension()
        if extension == ".jpg" or extension == ".jpeg" or extension == ".png" or extension == ".bmp":
            return "/static/media/file_icons/jpg.png"
        elif extension == ".doc" or extension == ".docx" or extension == ".xlsx" or extension == ".xls":
            return "/static/media/file_icons/doc.png"
        elif extension == ".pdf":
            return "/static/media/file_icons/pdf.png"
        elif extension == ".zip" or extension == ".rar" or extension == ".7z":
            return "/static/media/file_icons/zip.png"
        elif extension == ".txt":
            return "/static/media/file_icons/txt.png"
        else:
            return "/static/media/file_icons/data.png"
