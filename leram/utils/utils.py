import datetime 
import os
import random
import string
import math

from django.db.models import Count, Sum, Avg
from django.utils import timezone
from django.utils.text import slugify

def random_integer_generator(size=12, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def random_routing_no_generator(size=9, chars=string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_last_month_data(today):
    '''
    Simple method to get the datetime objects for the 
    start and end of last month. 
    '''
    this_month_start = datetime.datetime(today.year, today.month, 1)
    last_month_end = this_month_start - datetime.timedelta(days=1)
    last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    return (last_month_start, last_month_end)


def get_month_data_range(months_ago=1, include_this_month=False):
    '''
    A method that generates a list of dictionaires 
    that describe any given amout of monthly data.
    '''
    today = datetime.datetime.now().today()
    dates_ = []
    if include_this_month:
        # get next month's data with:
        next_month = today.replace(day=28) + datetime.timedelta(days=4)
        # use next month's data to get this month's data breakdown
        start, end = get_last_month_data(next_month)
        dates_.insert(0, {
            "start": start.timestamp(),
            "end": end.timestamp(),
            "start_json": start.isoformat(),
            "end": end.timestamp(),
            "end_json": end.isoformat(),
            "timesince": 0,
            "year": start.year,
            "month": str(start.strftime("%B")),
            })
    for x in range(0, months_ago):
        start, end = get_last_month_data(today)
        today = start
        dates_.insert(0, {
            "start": start.timestamp(),
            "start_json": start.isoformat(),
            "end": end.timestamp(),
            "end_json": end.isoformat(),
            "timesince": int((datetime.datetime.now() - end).total_seconds()),
            "year": start.year,
            "month": str(start.strftime("%B"))
        })
    #dates_.reverse()
    return dates_ 


def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)

def get_ckimage_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def ckupload_filename(filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_ckimage_filename_ext(filename)
    return '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    # return "uploads/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)



def unique_account_number_generator(instance):
    """
    This is for a Django project with an account_number field
    """
    size = random.randint(9, 12)
    new_account_number = random_integer_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(account_number=new_account_number).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_account_number



def unique_client_identity_number_generator(instance):
    """
    This is for a Django project with a citizen identity_number carfield
    """
    size = random.randint(9, 10)
    new_identity_number = random_integer_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(identity_number=new_identity_number).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return "ANG-" + new_identity_number



def unique_ang_number(instance):
    size = random.randint(9, 12)
    new_ang_number = random_integer_generator(size=size)

def unique_routing_number_generator(instance):
    """
    This is for a Django project with an routing_number field
    """
    size = random.randint(9, 12)
    new_routing_number = random_integer_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(routing_number=new_routing_number).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_routing_number

def unique_online_pin_generator(instance):
    """
    This is for a Django project with an pin field
    """
    size = random.randint(4, 4)
    new_online_pin = random_integer_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(pin=new_online_pin).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_online_pin

def unique_key_generator(instance):
    """
    This is for a Django project with an key field
    """
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key

def unique_order_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
