from django.apps import AppConfig

class FreelancerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freelancer'

    def ready(self):
        import freelancer.signals  # Replace 'freelancer' with the name of your app
