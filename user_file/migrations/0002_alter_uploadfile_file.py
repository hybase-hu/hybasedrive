# Generated by Django 4.2.1 on 2023-12-27 19:16

from django.db import migrations, models
import user_file.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=user_file.models.user_upload_to_path),
        ),
    ]