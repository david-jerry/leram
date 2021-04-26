import sweetify

from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from leram.events.forms import RequestForm
from leram.events.models import Request, Event

# Create your views here.
class EventDetailView(DetailView):
    model = Event
    slug_field = "slug"
    slug_url_kwarg = "slug"

class ServiceRequestView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = "pages/service-request.html"
    success_url = "home"

    def form_valid(self, form):
        self.object = form.save()
        sweetify.success(
            self.request,
            "Request Submitted Successfully",
            text="Your request has been successfully submitted for one of our services, we shall respond to your email and reach you also with your phone number provided. \nThank You.",
            timerProgressBar="true",
            icon="success",
            timer=4500,
        )
        return super().form_valid(form)
