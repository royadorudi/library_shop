from django.apps import AppConfig


class NewsletterModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter_module'

    def ready(self):
        import newsletter_module.signals
