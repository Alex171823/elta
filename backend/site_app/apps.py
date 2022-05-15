from django.apps import AppConfig


class SiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_app'

    def ready(self):
        import site_app.signals  # noqa
