# Generated by Django 4.2.1 on 2023-12-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/media/default_profile.jpg', upload_to='media'),
        ),
    ]
