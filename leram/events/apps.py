from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    name = 'leram.events'
    verbose_name = _("Events")

    def ready(self):
        try:
            import leram.events.signals  # noqa F401
        except ImportError:
            pass
