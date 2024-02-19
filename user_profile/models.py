from django.contrib.auth.models import User
from django.db import models

FILE_QUOTA = (
    ('50', '50 MB'),
    ('500', '500 MB'),
    ('1000', '1000 MB'),
)


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True,
                                        default="profile_pictures/default_profile.jpg")
    description = models.TextField(blank=True)
    quota = models.CharField(max_length=6, choices=FILE_QUOTA, default=50)

    def is_space_available(self):
        my_files = self.user.my_files.all()
        reserved_files_size = 0
        for mf in my_files:
            reserved_files_size = reserved_files_size + mf.file.size

        return int(int(self.quota) * 1024 * 1024) - int(reserved_files_size)
