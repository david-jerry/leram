from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django import forms

from ckeditor.widgets import CKEditorWidget

from leram.events.models import Event, Reservation, Request

admin.site.register(Reservation)
admin.site.register(Request)

class EventAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Event
        fields = '__all__'

class EventAdmin(admin.ModelAdmin):
    list_per_page = 250
    form = EventAdminForm
    fieldsets = (
        (None, {"fields": ("title", "location", "image", "bg_image", "price", "content")}),
        (_("Date info"), {"fields": ("pub_date", "event_date")}),
        (_("Map info"), {"fields": ("map_lat", "map_lng")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "featured",
                )
            },
        ),
    )
    list_display = ["title", "event_date", "price", "closed"]
    search_fields = ["title", "price"]


admin.site.register(Event, EventAdmin)
