import os
import random

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    GenericIPAddressField,
    ImageField,
    IntegerField,
    IPAddressField,
    ManyToManyField,
    OneToOneField,
    Q,
    SlugField,
    URLField,
)

from model_utils.models import StatusModel, TimeStampedModel
from category.models import Category, Tag
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import  PhoneNumberField
import datetime

# Create your models here.
User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def events_file_path(instance, filename):
    return "events/{filename}".format(filename=filename)


class Event(TimeStampedModel):
    title = CharField(
        _("Event/Destination Title"), blank=False, null=True, max_length=255
    )
    location = CharField(
        _("Event/Destination Location"), blank=False, null=True, max_length=400
    )
    slug = SlugField(unique=True, null=True, blank=True, max_length=500)
    image = ResizedImageField(
        _("Upload Event/Destination Image"),
        quality=75,
        force_format="JPEG",
        size=[345, 425],
        crop=["middle", "center"],
        upload_to=events_file_path,
        null=True,
        blank=True,
    )
    bg_image = ResizedImageField(
        _("Upload Event/Destination Background Image"),
        quality=75,
        force_format="JPEG",
        size=[1920, 1280],
        crop=["middle", "center"],
        upload_to=events_file_path,
        null=True,
        blank=True,
    )
    price = DecimalField(
        _("Destination Travel Expenses"), decimal_places=2, default=0.0, max_digits=20
    )

    pub_date = DateField(
        _("Event/Destination Published Date"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=False,
    )
    event_date = DateTimeField(
        _("Event/Destination Date & Time"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=False,
    )
    content = RichTextField(_("About the Event/Destination"))
    map_lat = CharField(
        _("Map Latitude"),
        blank=False,
        null=True,
        max_length=7,
        help_text="Google online for the latitude of the location to get an accurate readding here. https://map.google.com",
    )
    map_lng = CharField(
        _("Map Longitude"),
        blank=False,
        null=True,
        max_length=7,
        help_text="Google online for the longitude of the location to get an accurate readding here. https://map.google.com",
    )
    booked = BooleanField(_("Have you booked"), default=False)
    featured = BooleanField(_("Featured Event"), default=False)

    def __str__(self):
        return self.title.title()

    @property
    def closed(self):
        if datetime.date.today() > self.event_date:
            return True


    def get_absolute_url(self):
        """Get url for event's detail view.

        Returns:
            str: URL for event's detail.

        """
        return reverse("events:detail", kwargs={"slug": self.slug})


class Reservation(TimeStampedModel):
    destination = ForeignKey(Event, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user.name} booked to {self.destination.title}"

class Request(TimeStampedModel):
    phone_regex = RegexValidator(regex=r"^\+?\d{9,15}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    SERVICES = (
        ('Concierge', _('Concierge Service')),
        ('Private', _('Private Jet Service')),
        ('Travel', _('Travel Management Service')),
        ('Event', _('Event Management Service')),
        ('Watercraft', _('Yatch/Watercraft Service')),
        ('Shopping', _('VIP Shopping Service')),
        ('Estate', _('Estate/Property Consultation Service')),
        ('Tickets', _('Event Tickets Service')),
        ('Other', _('Other Service')),
    )


    first_name = CharField(_("First Name"), max_length=250, null=True, blank=False)
    last_name = CharField(_("Last Name"), max_length=250, null=True, blank=False)
    email = EmailField(_("Your Email"), blank=False, null=True)
    phone_number = CharField(_("Your Phone Number"), validators=[phone_regex], blank=False, null=True, max_length=17)
    serv_date = DateField(_("Service Date"), auto_now=False, auto_now_add=False, null=True, blank=False)
    service = CharField(_("Select Service"), max_length=250, choices=SERVICES, default="Concierge", null=True, blank=False)
    about_me = CharField(_("Brief info about you"), max_length=500, null=True, blank=False)
    about_needs = CharField(_("About Your Needs"), max_length=500, null=True, blank=False)
    referals = CharField(_("How did you find us?"), max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} requested for {self.service}"
