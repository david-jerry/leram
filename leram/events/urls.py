from django.urls import path

from leram.events.views import (
  ServiceRequestView,
  EventDetailView,
  event_booked,
)

app_name = "events"
urlpatterns = [
    path("make-request/", view=ServiceRequestView.as_view(), name="request"),
    path("<slug>/", view=EventDetailView.as_view(), name="detail"),
    path('<reservation_id>/completed/', event_booked, name='booked'),
]
