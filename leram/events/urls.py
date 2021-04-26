from django.urls import path

from leram.events.views import (
  ServiceRequestView,
  EventDetailView,
)

app_name = "events"
urlpatterns = [
    path("make-request/", view=ServiceRequestView.as_view(), name="request"),
    path("<slug>/", view=EventDetailView.as_view(), name="detail"),
]
