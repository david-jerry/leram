from leram.events.models import Event
from django.utils import timezone


def latest_events(request):
    return {
        "latest_events": Event.objects.order_by("-pub_date").filter(
            registration=False,
        )[:3],
    }