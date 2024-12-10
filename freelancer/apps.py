from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freelancer'

    def ready(self):
        import freelancer.signals 
