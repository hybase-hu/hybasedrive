from django import forms
from django.forms import ModelForm, ClearableFileInput, FileInput

from user_file.models import UploadFile


class UploadFileForms(ModelForm):

    class Meta:
        model = UploadFile
        fields = ('file', 'description')

    def __init__(self, *args, **kwargs):
        super(UploadFileForms, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control bg-dark text-light'
