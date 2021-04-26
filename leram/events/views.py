import sweetify

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView

from leram.events.forms import RequestForm
from leram.events.models import Request, Event, Reservation
from django.core.exceptions import PermissionDenied
from django.contrib import messages

# Create your views here.
class EventDetailView(DetailView):
    model = Event
    slug_field = "slug"
    slug_url_kwarg = "slug"

    # def get_context_data(self, **kwargs):
    #     context = super(EventDetailView, self).get_context_data(**kwargs)
    #     res = Reservation.objects.get_or_create(destination__id=self.object.id)
    #     context['res'] = res
    #     return context


class ServiceRequestView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = "pages/service-request.html"
    success_url = "home"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(
            self.request,
            "Your request has been successfully submitted for one of our services, we shall respond to your email and reach you also with your phone number provided. \nThank You.",
        )
        return super().form_valid(form)


def event_booked(request, reservation_id):
    if not request.user.is_authenticated:
        return redirect("account_login")
    eve = get_object_or_404(Event, pk=reservation_id)
    event = Reservation.objects.filter(user=request.user)
    if event.exists():
        messages.info(
            request,
            "You had placed a reservation for {title} already. \nThank You.".format(
                title=eve.title.capitalize()
            ),
        )
    else:
        event_res = Reservation.objects.create(
            destination=eve, user=request.user, booked=True
        )
        messages.success(
            request,
            "Your reservation for {title} was successful. \n We shall contact you shortly. Thank You.".format(
                title=eve.title.capitalize()
            ),
        )

    return redirect("home")
