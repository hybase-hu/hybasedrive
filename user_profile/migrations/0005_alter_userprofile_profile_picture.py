# Generated by Django 4.2.1 on 2023-12-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default_profile.jpg', upload_to='profile_pictures'),
        ),
    ]
