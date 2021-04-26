from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from leram.utils.utils import (
    unique_routing_number_generator, 
    unique_account_number_generator, 
    random_string_generator, 
    unique_slug_generator,
    unique_key_generator,
    unique_online_pin_generator, 
    unique_client_identity_number_generator,
    get_filename)

from leram.events.models import Event

def pre_save_Event_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(pre_save_Event_signal, sender=Event) 
