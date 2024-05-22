from django.apps import AppConfig


class IncomeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'income_app'

    # def ready(self):
    #     import income_app.signals