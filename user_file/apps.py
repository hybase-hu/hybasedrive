from django.apps import AppConfig


class UserFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_file'

    def ready(self):
        import user_file.signals
