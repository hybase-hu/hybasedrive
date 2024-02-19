from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_profile.models import UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("[+] user profile created with user ", instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print("[+] user profile modified", profile)
        except Exception as e:
            UserProfile.objects.create(user=instance)
            print("[+] user profile created error ", e)
