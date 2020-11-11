from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "capstone2.home"
    verbose_name = _("Home")

    def ready(self):
        try:
            import capstone2.home.signals  # noqa F401
        except ImportError:
            pass
